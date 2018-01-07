# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import UnpackSDICOMDir


def test_UnpackSDICOMDir_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    config=dict(argstr='-cfg %s',
    mandatory=True,
    xor=('run_info', 'config', 'seq_config'),
    ),
    dir_structure=dict(argstr='-%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    log_file=dict(argstr='-log %s',
    ),
    no_info_dump=dict(argstr='-noinfodump',
    ),
    no_unpack_err=dict(argstr='-no-unpackerr',
    ),
    output_dir=dict(argstr='-targ %s',
    ),
    run_info=dict(argstr='-run %d %s %s %s',
    mandatory=True,
    xor=('run_info', 'config', 'seq_config'),
    ),
    scan_only=dict(argstr='-scanonly %s',
    ),
    seq_config=dict(argstr='-seqcfg %s',
    mandatory=True,
    xor=('run_info', 'config', 'seq_config'),
    ),
    source_dir=dict(argstr='-src %s',
    mandatory=True,
    ),
    spm_zeropad=dict(argstr='-nspmzeropad %d',
    ),
    subjects_dir=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = UnpackSDICOMDir.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value

