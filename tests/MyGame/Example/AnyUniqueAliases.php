<?php
// automatically generated by the FlatBuffers compiler, do not modify

namespace MyGame\Example;

class AnyUniqueAliases
{
    const NONE = 0;
    const M = 1;
    const TS = 2;
    const M2 = 3;

    private static $names = array(
        AnyUniqueAliases::NONE=>"NONE",
        AnyUniqueAliases::M=>"M",
        AnyUniqueAliases::TS=>"TS",
        AnyUniqueAliases::M2=>"M2",
    );

    public static function name($e)
    {
        if (!isset(self::$names[$e])) {
            throw new \OutOfRangeException("Unknown enum value '{$e}' for AnyUniqueAliases");
        }
        return self::$names[$e];
    }
}
