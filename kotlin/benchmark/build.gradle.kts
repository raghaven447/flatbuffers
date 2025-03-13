import tasks.*

plugins {
  id("convention.multiplatform")
  id("org.jetbrains.kotlinx.benchmark")
  id("io.morethan.jmhreport")
  id("de.undercouch.download")
}

group = "com.google.flatbuffers.jmh"
version = "2.0.0-SNAPSHOT"

// This plugin generates a static html page with the aggregation
// of all benchmarks ran. very useful visualization tool.
jmhReport {
  val baseFolder = project.file("build/reports/benchmarks/main").absolutePath
  val lastFolder = project.file(baseFolder).list()?.sortedArray()?.lastOrNull() ?: ""
  jmhResultPath = "$baseFolder/$lastFolder/jvm.json"
  jmhReportOutput = "$baseFolder/$lastFolder"
}

// For now we benchmark on JVM only
benchmark {
  configurations {
    this.getByName("main") {
      iterations = 5
      iterationTime = 300
      iterationTimeUnit = "ms"
      // uncomment for benchmarking JSON op only
      include(".*FlatbufferBenchmark.*")
    }
  }
  targets {
    register("jvm")
  }
}

kotlin {
  jvm {
    withJava()
  }

  sourceSets {
    jvmMain {
      kotlin.srcDir("src/jvmMain/generated/kotlin/")
      kotlin.srcDir("src/jvmMain/generated/java/")

      dependencies {
        implementation(kotlin("stdlib-common"))
        implementation(project(":flatbuffers-kotlin"))
        implementation(libs.kotlinx.benchmark.runtime)
        // json serializers
        implementation(libs.moshi.kotlin)
        implementation(libs.gson)
      }
    }
  }
}

java {
  sourceSets {
    val main by getting {
      java.srcDir("../../java/src/main/java")
    }
  }
}

// This task download all JSON files used for benchmarking
tasks.register<de.undercouch.gradle.tasks.download.Download>("downloadMultipleFiles") {
  // We are downloading json benchmark samples from serdes-rs project.
  // see: https://github.com/serde-rs/json-benchmark/blob/master/data
  val baseUrl = "https://github.com/serde-rs/json-benchmark/raw/master/data/"
  src(listOf("$baseUrl/canada.json", "$baseUrl/twitter.json", "$baseUrl/citm_catalog.json"))
  dest(File("${project.projectDir.absolutePath}/src/jvmMain/resources"))
  overwrite(false)
}

// Use the default greeting
tasks.register<GenerateFBTestClasses>("generateFBTestClassesKt") {
  inputFiles.setFrom("$projectDir/monster_test_kotlin.fbs")
  includeFolder.set("$rootDir/../tests/include_test")
  outputFolder.set("${projectDir}/src/jvmMain/generated/kotlin/")
  variants.addAll("kotlin-kmp")
}

tasks.register<GenerateFBTestClasses>("generateFBTestClassesJava") {
  inputFiles.setFrom("$projectDir/monster_test_java.fbs")
  includeFolder.set("$rootDir/../tests/include_test")
  outputFolder.set("${projectDir}/src/jvmMain/generated/java/")
  variants.addAll("kotlin")
}

project.tasks.forEach {
  if (it.name.contains("compileKotlin")) {
    it.dependsOn("generateFBTestClassesKt")
    it.dependsOn("generateFBTestClassesJava")
  }
}
