required = {
    "VSAV":{
        "hdr":2,
        "ade":0,
        "soff":1,
        "off":0,
        "inf":0,
        "med":0           
    },

    "VLM":{
        "hdr":0,
        "ade":0,
        "soff":0,
        "off":0,
        "inf":0,
        "med":1  
    },

    "AR":{
        "hdr":0,
        "ade":1, 
        "soff":0,
        "off":0,
        "inf":1,
        "med":1
    },
    
    "VLCG":{
        "hdr":0,
        "ade":0, 
        "soff":0,
        "off":1,
        "inf":0,
        "med":0
    },

    "VTP":{
        "hdr":1,
        "ade":0, 
        "soff":0,
        "off":0,
        "inf":0,
        "med":0
    },

    "VL":{
        "hdr":1,
        "ade":0, 
        "soff":0,
        "off":0,
        "inf":0,
        "med":0
    },

    "VLHR":{
        "hdr":1,
        "ade":0, 
        "soff":0,
        "off":1,
        "inf":0,
        "med":0
    },

    "VLTT":{
        "hdr":1,
        "ade":0, 
        "soff":0,
        "off":0,
        "inf":0,
        "med":0
    },

    "VEMAH":{
        "hdr":2,
        "ade":0, 
        "soff":2,
        "off":0,
        "inf":0,
        "med":0
    },

    "VTUTP":{
        "hdr":1,
        "ade":0, 
        "soff":1,
        "off":0,
        "inf":0,
        "med":0
    },

    "CCGC":{
        "hdr":1,
        "ade":0, 
        "soff":1,
        "off":0,
        "inf":0,
        "med":0
    },
    
    "FPTL":{
        "hdr":2,
        "ade":0, 
        "soff":2,
        "off":0,
        "inf":0,
        "med":0
    },

    "FPTSR":{
        "hdr":3,
        "ade":0, 
        "soff":2,
        "off":1,
        "inf":0,
        "med":0
    },

    "EPA":{
        "hdr":1,
        "ade":0, 
        "soff":1,
        "off":0,
        "inf":0,
        "med":0
    },
    
    "CCF":{
        "hdr":2,
        "ade":0, 
        "soff":2,
        "off":0,
        "inf":0,
        "med":0
    },

    "VPC":{
        "hdr":1,
        "ade":0, 
        "soff":0,
        "off":2,
        "inf":0,
        "med":0
    },

    "VPMA":{
        "hdr":1,
        "ade":1, 
        "soff":1,
        "off":0,
        "inf":1,
        "med":1
    }
}

calculation = {
   "VSAV":{
        "hdr":["hdr"],
        "ade":[""], 
        "soff":["soff", "inf"],
        "off":["off", "med"],
        "inf":[""],
        "med":[""]
    },

    "VLM":{
        "hdr":["hdr"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":["inf"],
        "med":["med"]
    },

    "AR":{
        "hdr":["hdr"],
        "ade":["ade"],
        "soff":["soff"],
        "off":["off"],
        "inf":["inf"],
        "med":["med"]   
    },

    "VPMA":{
        "hdr":["hdr"],
        "ade":["ade"],
        "soff":["soff"],
        "off":["off"],
        "inf":["inf"],
        "med":["med"]   
    },

    "VLCG":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VTP":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VL":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VLTT":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VLHR":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VEMAH":{
        "hdr":["hdr"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VTUTP":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "CCGC":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "FPTL":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "FPTSR":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "EPA":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "CCF":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    },

    "VPC":{
        "hdr":["hdr", "inf", "med"],
        "ade":[""],
        "soff":["soff"],
        "off":["off"],
        "inf":[""],
        "med":[""]   
    }
    
}

