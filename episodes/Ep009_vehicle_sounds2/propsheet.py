import sys; sys.path.insert(0,'.')
from props import *
t=open('/home/claude/golu_pipeline/gen_episode_template.py').read()
F3D=t[t.index('<filter id="f3d"'):t.index('</filter>')+9]
items=[(aeroplane("p"),540,260,.9),(ambulance("a"),300,700,.85),(digger("d"),760,720,.75),(auto_rickshaw("u"),330,1120,.9)]
body="".join(f'<g transform="translate({x},{y}) scale({s})" filter="url(#f3d)">{b}</g>' for b,x,y,s in items)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1250" width="1080" height="1250"><defs>{PROP_DEFS}{F3D}</defs><rect width="1080" height="1250" fill="#bfe9ff"/>{body}</svg>'
open('prod/05_propsheet.svg','w').write(svg)
