// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var male = 0;
var female = 0;
var gender_data = gender_data; // gender_data called in the blade file


for (let i = 0; i < gender_data.length; i++) {
   
  if(gender_data[i].gender == "Man"){

      male = gender_data[i].count; 

  }else if(gender_data[i].gender == "Woman"){

      female = gender_data[i].count; 

  }

}

var kid = 0;
var teenage = 0;
var adult = 0;
var elder = 0;

var age_category_data = age_category_data; // age_category_data called in the blade file

for (let i = 0; i < age_category_data.length; i++) {
   
  if(age_category_data[i].age_category == "Kid"){
    
      kid = age_category_data[i].count; 

  }else if(age_category_data[i].age_category == "Teenage"){
  
      teenage = age_category_data[i].count; 

  }else if(age_category_data[i].age_category == "Adult"){
  
      adult = age_category_data[i].count; 

  }else if(age_category_data[i].age_category == "Elder"){
  
      elder = age_category_data[i].count; 

  }

}

var neutral = 0;
var happy = 0;
var sad = 0;
var angry = 0;
var fear = 0;
var surprise = 0;
var emotion_data = emotion_data; // emotion_data called in the blade file



for (let i = 0; i < emotion_data.length; i++) {
   
  if(emotion_data[i].emotion == "Neutral"){
    
      neutral = emotion_data[i].count; 

  }else if(emotion_data[i].emotion == "Happy"){
  
      happy = emotion_data[i].count; 

  }else if(emotion_data[i].emotion == "Sad"){
  
      sad = emotion_data[i].count; 

  }else if(emotion_data[i].emotion == "Angry"){
  
      angry = emotion_data[i].count; 

  }else if(emotion_data[i].emotion == "Fear"){
  
      fear = emotion_data[i].count; 

  }else if(emotion_data[i].emotion == "Surprise"){
  
      surprise = emotion_data[i].count; 

  }
  
}

var mask = 0;
var non_mask = 0;
var mask_data = mask_data; // mask_data called in the blade file


for (let i = 0; i < mask_data.length; i++) {
   
  if(mask_data[i].mask == "Found"){

      mask = mask_data[i].count; 

  }else if(mask_data[i].mask == "Not Found"){

      non_mask = mask_data[i].count; 

  }

}



var asian = 0;
var white = 0;
var black = 0;
var race_data = race_data; // race_data called in the blade file


for (let i = 0; i < race_data.length; i++) {
   
  if(race_data[i].race == "Asian"){ 

      asian = race_data[i].count; 

  }else if(race_data[i].race == "White"){

      white = race_data[i].count; 

  }else if(race_data[i].race == "Black"){

    black = race_data[i].count; 

  }

}


var sentiment_positive = 0;
var sentiment_negative = 0;
var sentiment_neutral = 0;
var sentiment_data = sentiment_data; // sentiment_data called in the blade file


for (let i = 0; i < sentiment_data.length; i++) {
   
  if(sentiment_data[i].prediction == "Positive"){ 

    sentiment_positive = sentiment_data[i].count; 

  }else if(sentiment_data[i].prediction == "Negative"){

    sentiment_negative = sentiment_data[i].count; 

  }else if(sentiment_data[i].prediction == "Neutral"){

    sentiment_neutral = sentiment_data[i].count; 

  }

}


// Pie Chart Example
var ctx = document.getElementById("gender-chart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Male", "Female"],
    datasets: [{
      data: [male, female],
      backgroundColor: ['#430eef', '#e754a5'],
      hoverBackgroundColor: ['#5d38ff', '#f389bd'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// Pie Chart Example
var ctx = document.getElementById("age_group");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Kids', 'Teenagers', 'Adults', 'Elders'],
    datasets: [{
      data: [kid, teenage, adult, elder],
      backgroundColor: ['#0220b7', '#127542','#b2bc24', '#c25012'],
      hoverBackgroundColor: ['#6d7cce', '#169a5b', '#d4db4a', '#e96f3c'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

// Pie Chart Example
var ctx = document.getElementById("emotion");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Neutral', 'Happy', 'Sad', 'Angery', 'Fear', 'Surprise'],
    datasets: [{
      data: [neutral, happy, sad, angry, fear ,surprise], 
      backgroundColor: ['#0220b7', '#127542','#030400', '#ee1616', '#81695d', '#386772' ],
      hoverBackgroundColor: ['#6d7cce', '#169a5b', '#4b4d4b', '#ff3838', '#a28b7e', '#57849c'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// Pie Chart Example
var ctx = document.getElementById("mask");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Mask", "Non-Masn"],
    datasets: [{
      data: [mask, non_mask],
      backgroundColor: ['#0220b7', '#f51c0c'],
      hoverBackgroundColor: ['#6d7cce', '#ff5a4d'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


// Pie Chart Example
var ctx = document.getElementById("race");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Asian', 'White', 'Black'],
    datasets: [{
      data: [asian, white, black],
      backgroundColor: ['#0220b7', '#f6e8c3', '#030001'],
      hoverBackgroundColor: ['#6d7cce', '#f9ecd6', '#4b4d4b'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});




// Pie Chart Example
var ctx = document.getElementById("sentiment_analysis");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Positive', 'Negative', 'Neutral'],
    datasets: [{
      data: [sentiment_positive, sentiment_negative, sentiment_neutral],
      backgroundColor: ['#0220b7', '#fe3737', '#169a5b'],
      hoverBackgroundColor: ['#6d7cce', '#ff7070', '#127542'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});



