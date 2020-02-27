function validateHost(string){
    if (string.indexOf(" ") >= 0) return false;
    string_spl = string.split(".");
    if (string_spl.length != 4) return false;
    for (i in string_spl){
        if (string_spl[i].isNaN()){
            return false;
        }
        else{
            if (parseInt(string_spl[i]) > 255){
                return false;
            }
        }
    }
    return (true);
}

function validateMac(string){
    if (string.indexOf(" ") >= 0) return false;
    string_spl = string.split(":")
    if (string_spl.length == 1){
        if (string.length != 12){
            return false;
        }
    }
    else{
        if (string_spl.length != 6){
            return false;
        }
        if (string.length != 17){
            return false;
        }
        for(i in string_spl){
            if (string_spl[i].length != 2){
                return false;
            }
        }
    }
    return true;
}

function validateID(string){
    if (string.indexOf(" ") >= 0) return false;
    return true;
}

function validateNumber(string){
    if (string.isNaN() == true){
        return false;
    }
    return true;
}

function change_alias(alias) {
    var str = alias;
    str = str.toLowerCase();
    str = str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g,"a"); 
    str = str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g,"e"); 
    str = str.replace(/ì|í|ị|ỉ|ĩ/g,"i"); 
    str = str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g,"o"); 
    str = str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g,"u"); 
    str = str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g,"y"); 
    str = str.replace(/đ/g,"d");
    str = str.replace(/!|@|%|\^|\*|\(|\)|\+|\=|\<|\>|\?|\/|,|\.|\:|\;|\'|\"|\&|\#|\[|\]|~|\$|_|`|-|{|}|\||\\/g," ");
    str = str.replace(/ + /g," ");
    str = str.trim(); 
    return str;
}

function join_word(string){
    var string_spl = string.split(" ");
    var result = string_spl.join("_");
    return result;
}