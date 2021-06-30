/*
 Regula: An annotation-based form-validation framework in Javascript
 Version 1.2.4-SNAPSHOT
 Written By Vivin Paliath (http://vivin.net)
 License: BSD License
 TODO: Add step validation to regula (like html5 step validation)
 TODO: Add URL validation to regula (like html5 url validation)
 Copyright (C) 2010-2012
 */


// checking name, country
regula.custom({
    name:'AlphaSpecial',
    defaultMessage: "The text field can only contain letters!",
    validator:function(){
        return /^[a-zA-Z'][a-zA-Z-' ]+[a-zA-Z']?$/.test(this.value)
    }
})
// check phones and faxes
regula.custom({
    name:'Phone',
    defaultMessage: "The text field can only contain phones numbers!",
    validator:function(){
        return /^\+?(\d[\d\-\+\(\) ]{5,}\d$)/.test(this.value)
    }
})
// check date format
regula.custom({
    name:'Date',
    defaultMessage: "The text field can only contain data format MM/DD/YY!",
    validator:function(){
        return /^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[13-9]|1[0-2])(\/|-|\.)(?:29|30)\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/.test(this.value)
    }
})
// check radioGroup selected range
regula.custom({
   name: "RadioGroupChecked",
   formSpecific: false,
   params: ["name"],
   defaultMessage: "You need to select at least one value!",
   validator: function(params) {
       var valid = false;
       jQuery("input[name=" + params["name"] + "]").each(function() {
           if(jQuery(this).is(":checked")) {
              valid = true;
           }
       });
       return valid;
   }
});