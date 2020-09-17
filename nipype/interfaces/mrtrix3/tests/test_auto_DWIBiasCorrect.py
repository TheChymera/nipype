# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import DWIBiasCorrect


def test_DWIBiasCorrect_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        bias=dict(
            argstr="-bias %s",
            extensions=None,
        ),
        bval_scale=dict(
            argstr="-bvalue_scaling %s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        grad_file=dict(
            argstr="-grad %s",
            extensions=None,
            xor=["grad_fsl"],
        ),
        grad_fsl=dict(
            argstr="-fslgrad %s %s",
            xor=["grad_file"],
        ),
        in_bval=dict(
            extensions=None,
        ),
        in_bvec=dict(
            argstr="-fslgrad %s %s",
            extensions=None,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        in_mask=dict(
            argstr="-mask %s",
            extensions=None,
        ),
        nthreads=dict(
            argstr="-nthreads %d",
            nohash=True,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            keep_extension=True,
            name_source="in_file",
            name_template="%s_biascorr",
            position=-1,
        ),
        use_ants=dict(
            argstr="-ants",
            mandatory=True,
            xor=["use_fsl"],
        ),
        use_fsl=dict(
            argstr="-fsl",
            mandatory=True,
            xor=["use_ants"],
        ),
    )
    inputs = DWIBiasCorrect.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DWIBiasCorrect_outputs():
    output_map = dict(
        bias=dict(
            extensions=None,
        ),
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = DWIBiasCorrect.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
