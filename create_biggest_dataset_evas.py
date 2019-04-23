import pandas as pd 
'''
#post
pbp_post_2009 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2009.csv')
pbp_post_2010 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2010.csv')
pbp_post_2011 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2011.csv')
pbp_post_2012 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2012.csv')
pbp_post_2013 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2013.csv')
pbp_post_2014 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2014.csv')
pbp_post_2015 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2015.csv')
pbp_post_2016 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2016.csv')
pbp_post_2017 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2017.csv')
pbp_post_2018 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/post_season/post_pbp_2018.csv')
#pre
pbp_pre_2009 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2009.csv')
pbp_pre_2010 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2010.csv')
pbp_pre_2011 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2011.csv')
pbp_pre_2012 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2012.csv')
pbp_pre_2013 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2013.csv')
pbp_pre_2014 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2014.csv')
pbp_pre_2015 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2015.csv')
pbp_pre_2016 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2016.csv')
pbp_pre_2017 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2017.csv')
pbp_pre_2018 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/pre_season/pre_pbp_2018.csv')
#reg
pbp_reg_2009 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2009.csv')
pbp_reg_2010 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2010.csv')
pbp_reg_2011 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2011.csv')
pbp_reg_2012 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2012.csv')
pbp_reg_2013 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2013.csv')
pbp_reg_2014 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2014.csv')
pbp_reg_2015 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2015.csv')
pbp_reg_2016 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2016.csv')
pbp_reg_2017 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2017.csv')
'''
pbp_reg_2018 = pd.read_csv('https://raw.githubusercontent.com/ryurko/nflscrapR-data/master/play_by_play_data/regular_season/reg_pbp_2018.csv')

# pbp = pd.concat([pbp_post_2009,pbp_post_2010,pbp_post_2011,pbp_post_2012,pbp_post_2013,pbp_post_2014,pbp_post_2015,pbp_post_2016,pbp_post_2017,pbp_post_2018,
#                  pbp_pre_2009,pbp_pre_2010,pbp_pre_2011,pbp_pre_2012,pbp_pre_2013,pbp_pre_2014,pbp_pre_2015,pbp_pre_2016,pbp_pre_2017,pbp_pre_2018,
#                  pbp_reg_2009,pbp_reg_2010,pbp_reg_2011,pbp_reg_2012,pbp_reg_2013,pbp_reg_2014,pbp_reg_2015,pbp_reg_2016,pbp_reg_2017,pbp_reg_2018], sort=False)

pbp_reg_2018.to_csv('pbp.csv', sep=',', encoding='utf-8')