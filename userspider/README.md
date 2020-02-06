## README

This file is a discription for configuration.

```
{
    "user_id_list": "./userid",
    "filter": 0,  // 0 means download all retweet content, otherwise don't 
    "since_date": "2019-12-10",
    "write_mode": ["csv"], // ['csv', 'json', 'mongo', 'mysql']
    "original_pic_download": 1,
    "retweet_pic_download": 0,
    "original_video_download": 1,
    "retweet_video_download": 0,
    "db_config": "", // for mysql, you need to fill in you mysql config; for mongo; the config is the authentication URL
    "cookie": ""
}
```


## References

1. https://patents.google.com/patent/CN102708176B/zh
2. https://github.com/dataabc/weibo-crawler
3. https://github.com/SpiderClub/weibospider
4. 
