# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..diffusion import DTIimport


def test_DTIimport_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputFile=dict(
            argstr="%s",
            extensions=None,
            position=-2,
        ),
        outputTensor=dict(
            argstr="%s",
            hash_files=False,
            position=-1,
        ),
        testingmode=dict(
            argstr="--testingmode ",
        ),
    )
    inputs = DTIimport.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DTIimport_outputs():
    output_map = dict(
        outputTensor=dict(
            extensions=None,
            position=-1,
        ),
    )
    outputs = DTIimport.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
