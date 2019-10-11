#利用Overlap叠加Line+EffectScatter(带有涟漪特效动画的散点图)
from pyecharts import Line, EffectScatter, Overlap
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"] 
v1 = [5, 20, 36, 10, 10, 100] 
line = Line("line - es 示例") 
line.add("", attr, v1, is_random=True) 
es = EffectScatter() 
es.add("", attr, v1, effect_scale=8)
overlap = Overlap() 
overlap.add(line) 
overlap.add(es)
overlap.render()