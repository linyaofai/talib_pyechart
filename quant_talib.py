import talib
import tushare
from pyecharts import Line, Kline, Bar, Overlap, Grid,EffectScatter
data = tushare.get_k_data('600519', ktype='D', autype='None', start='2016-01-01', end='2019-10-01')

# 定义k线图的提示框的显示函数
def show_kline_data(params, pos):
    param = params[0]
    if param.data[4]:
        return "date = " + param.name + "<br/>" + "open = " + param.data[1] + "<br/>" + "close = " + param.data[
    2] + "<br/>" + "high = " + param.data[3] + "<br/>" + "low = " + param.data[
       4] + "<br/> "
    else:
        return "date = " + param.name + "<br/>" + "cci = " + param.value + "<br/>"

# 画出K线图
price = [[open, close, lowest, highest] for open, close, lowest, highest in
 zip(data['open'], data['close'], data['low'], data['high'])]
kline = Kline("贵州茅台", title_pos='center')
kline.add('日线', x_axis=data['date'], y_axis=price, is_datazoom_show=True,
  is_xaxislabel_align=True,
  tooltip_tragger='axis',
  yaxis_pos='left',
  legend_top="20%",
  legend_orient='vertical',
  legend_pos='right',
  is_toolbox_show=True,
  tooltip_formatter=show_kline_data)

# kline.render()
cci = talib.CCI(data['high'].values, data['low'].values, data['close'].values, timeperiod=14)

line = Line("cci")
line.add("", x_axis=data['date'], y_axis=cci, is_random=True)
# es = EffectScatter()
# es.add("", data['date'], cci, effect_scale=8)
overlap = Overlap()
overlap.add(line)
overlap.add(kline)
overlap.render()