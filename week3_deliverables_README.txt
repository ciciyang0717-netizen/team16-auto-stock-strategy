
# Team 16 - Week 3 交付物

## 已完成工作
1. **数据清洗**：处理了所有缺失值，确保数据质量
2. **因子标准化**：对所有技术因子进行Z-Score标准化
3. **EDA可视化**：生成了4类关键图表

## 生成的文件
- `auto_stock_clean_data.csv`: 清洗后的完整数据
- `factor_summary_stats.csv`: 因子统计摘要
- `correlation_heatmap.png`: 相关性热力图
- `factor_distributions.png`: 因子分布箱线图
- `time_series.png`: 时间序列走势图
- `scatter_plots.png`: 截面散点图

## 关键发现
1. 股票间收益率相关性不高（<0.22），适合做排名预测
2. 不同股票的因子分布存在显著差异
3. RSI和动量因子在不同股票上的表现不同
