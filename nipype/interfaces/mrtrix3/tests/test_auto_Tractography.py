# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..tracking import Tractography


def test_Tractography_inputs():
    input_map = dict(act_file=dict(argstr='-act %s',
    ),
    algorithm=dict(argstr='-algorithm %s',
    usedefault=True,
    ),
    angle=dict(argstr='-angle %f',
    ),
    args=dict(argstr='%s',
    ),
    backtrack=dict(argstr='-backtrack',
    ),
    bval_scale=dict(argstr='-bvalue_scaling %s',
    ),
    crop_at_gmwmi=dict(argstr='-crop_at_gmwmi',
    ),
    cutoff=dict(argstr='-cutoff %f',
    ),
    cutoff_init=dict(argstr='-initcutoff %f',
    ),
    downsample=dict(argstr='-downsample %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    grad_file=dict(argstr='-grad %s',
    ),
    grad_fsl=dict(argstr='-fslgrad %s %s',
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_bval=dict(),
    in_bvec=dict(argstr='-fslgrad %s %s',
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    init_dir=dict(argstr='-initdirection %f,%f,%f',
    ),
    max_length=dict(argstr='-maxlength %f',
    ),
    max_seed_attempts=dict(argstr='-max_seed_attempts %d',
    ),
    max_tracks=dict(argstr='-maxnum %d',
    ),
    min_length=dict(argstr='-minlength %f',
    ),
    n_samples=dict(argstr='-samples %d',
    ),
    n_tracks=dict(argstr='-number %d',
    ),
    n_trials=dict(argstr='-trials %d',
    ),
    noprecompt=dict(argstr='-noprecomputed',
    ),
    nthreads=dict(argstr='-nthreads %d',
    nohash=True,
    ),
    out_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    out_seeds=dict(argstr='-output_seeds %s',
    ),
    power=dict(argstr='-power %d',
    ),
    roi_excl=dict(argstr='-exclude %s',
    ),
    roi_incl=dict(argstr='-include %s',
    ),
    roi_mask=dict(argstr='-mask %s',
    ),
    seed_dynamic=dict(argstr='-seed_dynamic %s',
    ),
    seed_gmwmi=dict(argstr='-seed_gmwmi %s',
    requires=['act_file'],
    ),
    seed_grid_voxel=dict(argstr='-seed_grid_per_voxel %s %d',
    xor=['seed_image', 'seed_rnd_voxel'],
    ),
    seed_image=dict(argstr='-seed_image %s',
    ),
    seed_rejection=dict(argstr='-seed_rejection %s',
    ),
    seed_rnd_voxel=dict(argstr='-seed_random_per_voxel %s %d',
    xor=['seed_image', 'seed_grid_voxel'],
    ),
    seed_sphere=dict(argstr='-seed_sphere %f,%f,%f,%f',
    ),
    sph_trait=dict(argstr='%f,%f,%f,%f',
    ),
    step_size=dict(argstr='-step %f',
    ),
    stop=dict(argstr='-stop',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    unidirectional=dict(argstr='-unidirectional',
    ),
    use_rk4=dict(argstr='-rk4',
    ),
    )
    inputs = Tractography.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Tractography_outputs():
    output_map = dict(out_file=dict(),
    out_seeds=dict(),
    )
    outputs = Tractography.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
