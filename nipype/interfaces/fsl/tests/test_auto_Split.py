# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Split


def test_Split_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dimension=dict(argstr='-%s',
    mandatory=True,
    position=2,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=0,
    ),
    out_base_name=dict(argstr='%s',
    position=1,
    ),
    output_type=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = Split.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Split_outputs():
    output_map = dict(out_files=dict(),
    )
    outputs = Split.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
