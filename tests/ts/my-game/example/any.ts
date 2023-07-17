// automatically generated by the FlatBuffers compiler, do not modify

import * as flatbuffers from 'flatbuffers';

import { Monster as MyGame_Example2_Monster, monsterVerify as myGameExample2MonsterVerify, MonsterT as MyGame_Example2_MonsterT } from '../../my-game/example2/monster.js';
import { Monster, monsterVerify, MonsterT } from '../../my-game/example/monster.js';
import { TestSimpleTableWithEnum, testSimpleTableWithEnumVerify, TestSimpleTableWithEnumT } from '../../my-game/example/test-simple-table-with-enum.js';


export enum Any {
  NONE = 0,
  Monster = 1,
  TestSimpleTableWithEnum = 2,
  MyGame_Example2_Monster = 3
}

export function unionToAny(
  type: Any,
  accessor: (obj:Monster|MyGame_Example2_Monster|TestSimpleTableWithEnum) => Monster|MyGame_Example2_Monster|TestSimpleTableWithEnum|null
): Monster|MyGame_Example2_Monster|TestSimpleTableWithEnum|null {
  switch(Any[type]) {
    case 'NONE': return null; 
    case 'Monster': return accessor(new Monster())! as Monster;
    case 'TestSimpleTableWithEnum': return accessor(new TestSimpleTableWithEnum())! as TestSimpleTableWithEnum;
    case 'MyGame_Example2_Monster': return accessor(new MyGame_Example2_Monster())! as MyGame_Example2_Monster;
    default: return null;
  }
}

export function unionListToAny(
  type: Any, 
  accessor: (index: number, obj:Monster|MyGame_Example2_Monster|TestSimpleTableWithEnum) => Monster|MyGame_Example2_Monster|TestSimpleTableWithEnum|null, 
  index: number
): Monster|MyGame_Example2_Monster|TestSimpleTableWithEnum|null {
  switch(Any[type]) {
    case 'NONE': return null; 
    case 'Monster': return accessor(index, new Monster())! as Monster;
    case 'TestSimpleTableWithEnum': return accessor(index, new TestSimpleTableWithEnum())! as TestSimpleTableWithEnum;
    case 'MyGame_Example2_Monster': return accessor(index, new MyGame_Example2_Monster())! as MyGame_Example2_Monster;
    default: return null;
  }
}

export function anyVerify(verifier: flatbuffers.Verifier, typeId: number, tablePos: flatbuffers.UOffset) : boolean{
  let result: boolean = false
  switch(Any[typeId]) {
    case 'Monster':
      result = monsterVerify(verifier, tablePos);
      break;
    case 'TestSimpleTableWithEnum':
      result = testSimpleTableWithEnumVerify(verifier, tablePos);
      break;
    case 'MyGame_Example2_Monster':
      result = myGameExample2MonsterVerify(verifier, tablePos);
      break;
    default: result = true;
  }
  return result;
}
