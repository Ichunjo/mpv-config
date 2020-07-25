from lvsfunc.denoise import detail_mask
import vapoursynth as vs
core = vs.core

clip = video_in

dither = core.resize.Bicubic(clip, format=vs.YUV420P16)

line_m = detail_mask(dither, brz_a=3000, brz_b=1500)
db = core.neo_f3kdb.Deband(dither, 17, 56, 48, 48, 24, 0, 2, keep_tv_range=True)
db = core.std.MaskedMerge(db, dither, line_m)
grain = core.grain.Add(db, 1, constant=False)
out = core.resize.Bicubic(grain, format=vs.YUV420P8, dither_type='error_diffusion')

out.set_output()
