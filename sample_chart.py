dict ={

    "chart": {
        "type": 'column'
    },

    "title": {
        "text": 'Olympic Games all-time medal table, grouped by continent',
        "align": 'left'
    },

    "xAxis": {
        "categories": ['Gold', 'Silver', 'Bronze']
    },

    "yAxis": {
        "allowDecimals": False,
        "min": 0,
        "title": {
            "text": 'Count medals'
        }
    },

    "tooltip": {
        "format": '<b>{key}</b><br/>{series.name}: {y}<br/>' +
            'Total: {point.stackTotal}'
    },

    "plotOptions": {
        "column": {
            "stacking": 'normal'
        }
    },

    "series": [{
        "name": 'Female',
        "data": [148, 133, 124]
    }, {
        "name": 'male',
        "data": [102, 98, 65]
    }]
}

sample_es_data = {
  "took" : 16,
  "timed_out" : False,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1050,
    "max_score" : 0.0,
    "hits" : [ ]
  },
  "aggregations" : {
    "NAME" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "FEMALE",
          "doc_count" : 533,
          "NAME" : {
            "doc_count_error_upper_bound" : 0,
            "sum_other_doc_count" : 0,
            "buckets" : [
              {
                "key" : "Women's Clothing",
                "doc_count" : 428
              },
              {
                "key" : "Women's Shoes",
                "doc_count" : 235
              },
              {
                "key" : "Women's Accessories",
                "doc_count" : 152
              },
              {
                "key" : "Men's Clothing",
                "doc_count" : 14
              },
              {
                "key" : "Men's Shoes",
                "doc_count" : 7
              },
              {
                "key" : "Men's Accessories",
                "doc_count" : 4
              }
            ]
          }
        },
        {
          "key" : "MALE",
          "doc_count" : 517,
          "NAME" : {
            "doc_count_error_upper_bound" : 0,
            "sum_other_doc_count" : 0,
            "buckets" : [
              {
                "key" : "Men's Clothing",
                "doc_count" : 445
              },
              {
                "key" :"Men's Shoes",
                "doc_count" : 206
              },
              {
                "key" : "Men's Accessories",
                "doc_count" : 122
              },
              {
                "key" : "Women's Accessories",
                "doc_count" : 27
              }
            ]
          }
        }
      ]
    }
  }
}



# dict['title']['text'] ="Vijo"




# dict["xAxis"]["categories"].clear()
# dict["series"][0]["data"].clear()
# dict["series"][1]["data"].clear()

# for i in sample_es_data["aggregations"]["NAME"]["buckets"][0]["NAME"]["buckets"]:
#     dict["xAxis"]["categories"].append(i["key"])
#     dict["series"][0]["data"].append(i["doc_count"])

# for i in sample_es_data["aggregations"]["NAME"]["buckets"][1]["NAME"]["buckets"]:
#     dict["series"][1]["data"].append(i["doc_count"])

new_cat=[]
f_data=[]
m_data=[]
for i in sample_es_data["aggregations"]["NAME"]["buckets"]:
    for j in i["NAME"]["buckets"]:
        new_cat.append(j["key"])
        if i["key"] == "FEMALE":
            f_data.append(j["doc_count"])
        else:
            m_data.append(j["doc_count"])    


dict["xAxis"]["categories"]=new_cat
dict["series"][0]["data"]=f_data
dict["series"][1]["data"]=m_data


print(dict)    