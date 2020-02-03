// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace MyGame.Example
{

#if ENABLE_JSON_SERIALIZATION
  [Newtonsoft.Json.JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
#endif
public enum AnyAmbiguousAliases : byte
{
  NONE = 0,
  M1 = 1,
  M2 = 2,
  M3 = 3,
};

public class AnyAmbiguousAliasesUnion {
  public AnyAmbiguousAliases Type { get; set; }
  public object Value { get; set; }

  public AnyAmbiguousAliasesUnion() {
    this.Type = AnyAmbiguousAliases.NONE;
    this.Value = null;
  }

  public T As<T>() where T : class { return this.Value as T; }
  public MyGame.Example.MonsterT AsM1() { return this.As<MyGame.Example.MonsterT>(); }
  public MyGame.Example.MonsterT AsM2() { return this.As<MyGame.Example.MonsterT>(); }
  public MyGame.Example.MonsterT AsM3() { return this.As<MyGame.Example.MonsterT>(); }

  public static int Pack(FlatBuffers.FlatBufferBuilder builder, AnyAmbiguousAliasesUnion _o) {
    switch (_o.Type) {
      default: return 0;
      case AnyAmbiguousAliases.M1: return MyGame.Example.Monster.Pack(builder, _o.AsM1()).Value;
      case AnyAmbiguousAliases.M2: return MyGame.Example.Monster.Pack(builder, _o.AsM2()).Value;
      case AnyAmbiguousAliases.M3: return MyGame.Example.Monster.Pack(builder, _o.AsM3()).Value;
    }
  }
}

#if ENABLE_JSON_SERIALIZATION
public class AnyAmbiguousAliasesUnion_JsonConverter : Newtonsoft.Json.JsonConverter {
  public override bool CanConvert(System.Type objectType) {
    return objectType == typeof(AnyAmbiguousAliasesUnion) || objectType == typeof(System.Collections.Generic.List<AnyAmbiguousAliasesUnion>);
  }
  public override void WriteJson(Newtonsoft.Json.JsonWriter writer, object value, Newtonsoft.Json.JsonSerializer serializer) {
    var _olist = value as System.Collections.Generic.List<AnyAmbiguousAliasesUnion>;
    if (_olist != null) {
      writer.WriteStartArray();
      foreach (var _o in _olist) { this.WriteJson(writer, _o, serializer); }
      writer.WriteEndArray();
    } else {
      this.WriteJson(writer, value as AnyAmbiguousAliasesUnion, serializer);
    }
  }
  public void WriteJson(Newtonsoft.Json.JsonWriter writer, AnyAmbiguousAliasesUnion _o, Newtonsoft.Json.JsonSerializer serializer) {
    if (_o == null) return;
    serializer.Serialize(writer, _o.Value);
  }
  public override object ReadJson(Newtonsoft.Json.JsonReader reader, System.Type objectType, object existingValue, Newtonsoft.Json.JsonSerializer serializer) {
    var _olist = existingValue as System.Collections.Generic.List<AnyAmbiguousAliasesUnion>;
    if (_olist != null) {
      for (var _j = 0; _j < _olist.Count; ++_j) {
        reader.Read();
        _olist[_j] = this.ReadJson(reader, _olist[_j], serializer);
      }
      reader.Read();
      return _olist;
    } else {
      return this.ReadJson(reader, existingValue as AnyAmbiguousAliasesUnion, serializer);
    }
  }
  public AnyAmbiguousAliasesUnion ReadJson(Newtonsoft.Json.JsonReader reader, AnyAmbiguousAliasesUnion _o, Newtonsoft.Json.JsonSerializer serializer) {
    if (_o == null) return null;
    switch (_o.Type) {
      default: break;
      case AnyAmbiguousAliases.M1: _o.Value = serializer.Deserialize<MyGame.Example.MonsterT>(reader); break;
      case AnyAmbiguousAliases.M2: _o.Value = serializer.Deserialize<MyGame.Example.MonsterT>(reader); break;
      case AnyAmbiguousAliases.M3: _o.Value = serializer.Deserialize<MyGame.Example.MonsterT>(reader); break;
    }
    return _o;
  }
}
#endif


}
