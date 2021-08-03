// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

namespace MyGame.Example
{

[Newtonsoft.Json.JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
public enum Any : byte
{
  NONE = 0,
  Monster = 1,
  TestSimpleTableWithEnum = 2,
  MyGame_Example2_Monster = 3,
};

public class AnyUnion {
  public Any Type { get; set; }
  public object Value { get; set; }

  public AnyUnion() {
    this.Type = Any.NONE;
    this.Value = null;
  }

  public T As<T>() where T : class { return this.Value as T; }
  public global::MyGame.Example.MonsterT AsMonster() { return this.As<global::MyGame.Example.MonsterT>(); }
  public static AnyUnion FromMonster(global::MyGame.Example.MonsterT _monster) { return new AnyUnion{ Type = Any.Monster, Value = _monster }; }
  internal global::MyGame.Example.TestSimpleTableWithEnumT AsTestSimpleTableWithEnum() { return this.As<global::MyGame.Example.TestSimpleTableWithEnumT>(); }
  internal static AnyUnion FromTestSimpleTableWithEnum(global::MyGame.Example.TestSimpleTableWithEnumT _testsimpletablewithenum) { return new AnyUnion{ Type = Any.TestSimpleTableWithEnum, Value = _testsimpletablewithenum }; }
  public global::MyGame.Example2.MonsterT AsMyGame_Example2_Monster() { return this.As<global::MyGame.Example2.MonsterT>(); }
  public static AnyUnion FromMyGame_Example2_Monster(global::MyGame.Example2.MonsterT _mygame_example2_monster) { return new AnyUnion{ Type = Any.MyGame_Example2_Monster, Value = _mygame_example2_monster }; }

  public static int Pack(FlatBuffers.FlatBufferBuilder builder, AnyUnion _o) {
    switch (_o.Type) {
      default: return 0;
      case Any.Monster: return global::MyGame.Example.Monster.Pack(builder, _o.AsMonster()).Value;
      case Any.TestSimpleTableWithEnum: return global::MyGame.Example.TestSimpleTableWithEnum.Pack(builder, _o.AsTestSimpleTableWithEnum()).Value;
      case Any.MyGame_Example2_Monster: return global::MyGame.Example2.Monster.Pack(builder, _o.AsMyGame_Example2_Monster()).Value;
    }
  }
}

public class AnyUnion_JsonConverter : Newtonsoft.Json.JsonConverter {
  public override bool CanConvert(System.Type objectType) {
    return objectType == typeof(AnyUnion) || objectType == typeof(System.Collections.Generic.List<AnyUnion>);
  }
  public override void WriteJson(Newtonsoft.Json.JsonWriter writer, object value, Newtonsoft.Json.JsonSerializer serializer) {
    var _olist = value as System.Collections.Generic.List<AnyUnion>;
    if (_olist != null) {
      writer.WriteStartArray();
      foreach (var _o in _olist) { this.WriteJson(writer, _o, serializer); }
      writer.WriteEndArray();
    } else {
      this.WriteJson(writer, value as AnyUnion, serializer);
    }
  }
  public void WriteJson(Newtonsoft.Json.JsonWriter writer, AnyUnion _o, Newtonsoft.Json.JsonSerializer serializer) {
    if (_o == null) return;
    serializer.Serialize(writer, _o.Value);
  }
  public override object ReadJson(Newtonsoft.Json.JsonReader reader, System.Type objectType, object existingValue, Newtonsoft.Json.JsonSerializer serializer) {
    var _olist = existingValue as System.Collections.Generic.List<AnyUnion>;
    if (_olist != null) {
      for (var _j = 0; _j < _olist.Count; ++_j) {
        reader.Read();
        _olist[_j] = this.ReadJson(reader, _olist[_j], serializer);
      }
      reader.Read();
      return _olist;
    } else {
      return this.ReadJson(reader, existingValue as AnyUnion, serializer);
    }
  }
  public AnyUnion ReadJson(Newtonsoft.Json.JsonReader reader, AnyUnion _o, Newtonsoft.Json.JsonSerializer serializer) {
    if (_o == null) return null;
    switch (_o.Type) {
      default: break;
      case Any.Monster: _o.Value = serializer.Deserialize<global::MyGame.Example.MonsterT>(reader); break;
      case Any.TestSimpleTableWithEnum: _o.Value = serializer.Deserialize<global::MyGame.Example.TestSimpleTableWithEnumT>(reader); break;
      case Any.MyGame_Example2_Monster: _o.Value = serializer.Deserialize<global::MyGame.Example2.MonsterT>(reader); break;
    }
    return _o;
  }
}


}
