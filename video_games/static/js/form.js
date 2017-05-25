var optionsByCategory = {
    Platform: ["2600", "SAT", "3DS", "DC", "DS", "GB", "GBA", "GC", "GEN", "N64", "NES",
    "PC", "PS", "PS2", "PS3", "PS4", "PSP", "PSV", "SCD", "SNES", "Wii", "WiiU", "X360", "XB", "XOne"],
    Year: ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010", "2011", "2012", "2013", "2014",
     "2015", "2016", "2017", "2018", "2019", "2020"],
    Genre: ["Action", "Adventure", "Fighting", "Misc", "Platform", "Puzzle", "Racing", "Role-Playing",
     "Shooter", "Simulation", "Sports", "Strategy"],
    Publisher:["505 Games","989 Studios","Acclaim Entertainment","Activision","Activision Value","Arena Entertainment",
    "ASCII Entertainment","Atari","Banpresto","Capcom","Codemasters","Crave Entertainment","D3Publishers",
    "Deep Silver","Disney Interactive Studios","Eidos Interactive","Electronic Arts","Enix Corporation",
    "Fox Interactive","Global Star","Gotham Games","GT Interactive","GungHo","Hasbro Interactive","Hello Games",
    "Hudson Soft","Imagic","Infogrames","JVC","Konami Digital Entertainment","Level 5","LucasArts","Majesco Entertainment",
    "Maxis","Microsoft Game Studios","Mindway Games","MTV Games","N/A","Namco Bandai Games","NCSoft","Nintendo",
    "Oxygen Interactive","Palcom","Parker Bros.","Red Orb","Red Storm Entertainment","RedOctane","Sega",
    "Sony Computer Entertainment","Sony Computer Entertainment Europe","Square","Square Enix","SquareSoft",
    "Take-Two Interactive","Tecmo Koei","THQ","Ubisoft","UEP Systems","Universal Interactive","Unknown","Valve",
    "Valve Software","Video System","Virgin Interactive","Vivendi Games","Warner Bros. Interactive Entertainment",
    "Westwood Studios"]
}

var rcLabels = [ "Platform", "Year", "Genre","Publisher"]

// changes the filter value options based on the selection made
    function change(value) {
        if (value.length == 0 || value == "none") document.getElementById("options").innerHTML = "<option selected></option>";
        else {
            var catOptions = "";
            for (categoryId in optionsByCategory[value]) {
                catOptions += "<option>" + optionsByCategory[value][categoryId] + "</option>";
            }
            document.getElementById("options").innerHTML = catOptions;
        }
    }

//shows/ hides the warning/ability to continue based on the selections made for column
    function checkAlert1(value){
        var cat2Val = document.getElementById("cat2").value
        var x = document.getElementById('warning');
        if(value === cat2Val){
            x.style.display = 'block';
           document.getElementById('submit').disabled = true;
           document.getElementById('submit').innerHTML = 'Waiting ... ';
        } else{
            x.style.display = 'none';
            document.getElementById('submit').disabled = false;
             document.getElementById('submit').innerHTML = 'Game Start!';
        }
    }

//shows/hides warning / ability to continue based on row selections
    function checkAlert2(value){
        var cat1Val = document.getElementById("cat1").value
        var x = document.getElementById('warning');
        if(value === cat1Val){
            x.style.display = 'block';
            document.getElementById('submit').disabled = true;
           document.getElementById('submit').innerHTML = 'Waiting ... ';
        } else{
            x.style.display = 'none';
            document.getElementById('submit').disabled = false;
             document.getElementById('submit').innerHTML = 'Game Start!';
        }
    }