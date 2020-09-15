import placebo # https://github.com/Ichunjo/vardefunc/blob/master/placebo.py

from vsutil import depth

import lvsfunc as lvf # https://github.com/Irrational-Encoding-Wizardry/lvsfunc
import vapoursynth as vs # https://github.com/vapoursynth/vapoursynth/releases
core = vs.core

clip = video_in

dither = depth(clip, 16)

lineart_mask = lvf.denoise.detail_mask(dither, brz_a=3000, brz_b=1500)

#deband = core.neo_f3kdb.Deband(dither, 17, 56, 48, 48, 24, 0, 2, keep_tv_range=True) # https://github.com/HomeOfAviSynthPlusEvolution/neo_f3kdb/releases
deband = placebo.deband(dither, 17, 5, 1, 0)
deband = core.std.MaskedMerge(deband, dither, lineart_mask)


grain = core.grain.Add(deband, 1, constant=False) # https://github.com/HomeOfVapourSynthEvolution/VapourSynth-AddGrain


out = depth(grain, 8)
# out = depth(grain, 10)

out.set_output()
