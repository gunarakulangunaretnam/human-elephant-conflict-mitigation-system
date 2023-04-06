@extends('dashboard-layout.base-template')

@section('content')

<div class="container-fluid">

    <!-- Page Heading -->

    <div class="row">
    
        <div class="jumbotron col-xl-12 col-lg-12" style="background-clip: #f8f9fc;">
            <div class="col-md-3 offset-md-3 col-lg-3 offset-lg-4">
                <div class="input-group input-group-sm mb-3">
                    <div class="input-group-prepend">
                        <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Filter by Month:</span>
                    </div>
                    <input type="month" value="{{$YearMonth}}" id="month_picker" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm">
                </div>
             </div>
        </div>

        <!-- Area Chart -->
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">

                
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Customer Traffic Tracker</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                    <div class="chart-area">
                        <canvas id="customer-chart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- Pie Chart -->
        <div class="col-xl-4 col-lg-5">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Gender</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                    <div class="chart-pie pt-4 pb-2">
                        <canvas id="gender-chart"></canvas>
                    </div>
                    <div class="mt-4 text-center small">
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#430eef;"></i> Male
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#e754a5;"></i> Female
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-xl-4 col-lg-5">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Age Group</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                    <div class="chart-pie pt-4 pb-2">
                        <canvas id="age_group"></canvas>
                    </div>
                    <div class="mt-4 text-center small">
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#0220b7;"></i> Kids
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#169a5b;"></i> Teenagers
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#b2bc24;"></i> Adults
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#c25012;"></i> Elders
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-xl-4 col-lg-5">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Emotion</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                    <div class="chart-pie pt-4 pb-2">
                        <canvas id="emotion"></canvas>
                    </div>
                    <div class="mt-4 text-center small">
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#0220b7;"></i> Natural
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#169a5b;"></i> Happy
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#030400;"></i> Sad
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#ee1616;"></i> Angery
                        </span>

                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#81695d;"></i> Fear
                        </span>

                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#386772;"></i> Surprise
                        </span>

                    </div>
                </div>
            </div>
        </div>

        <div class="col-xl-4 col-lg-5">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Mask</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body">
                    <div class="chart-pie pt-4 pb-2">
                        <canvas id="mask"></canvas>
                    </div>
                    <div class="mt-4 text-center small">
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#0220b7;"></i> Mask
                        </span>
                        <span class="mr-2">
                            <i class="fas fa-circle" style="color:#f51c0c;"></i> Non-Mask
                        </span>
                    </div>
                </div>
            </div>
        </div>


        
    <div class="col-xl-4 col-lg-5">
        <div class="card shadow mb-4">
            <!-- Card Header - Dropdown -->
            <div
                class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Race</h6>
            </div>
            <!-- Card Body -->
            <div class="card-body">
                <div class="chart-pie pt-4 pb-2">
                    <canvas id="race"></canvas>
                </div>
                <div class="mt-4 text-center small">
                    <span class="mr-2">
                        <i class="fas fa-circle" style="color:#0220b7;"></i> Asian
                    </span>
                    <span class="mr-2">
                        <i class="fas fa-circle" style="color:#f6e8c3;"></i> White
                    </span>
                    <span class="mr-2">
                        <i class="fas fa-circle" style="color:#030001;"></i> Black
                    </span>
                </div>
            </div>
        </div>
    </div>
                            
    <div class="col-xl-4 col-lg-5">
        <div class="card shadow mb-4">
            <!-- Card Header - Dropdown -->
            <div
                class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                <h6 class="m-0 font-weight-bold text-primary">Sentiment Analysis</h6>
            </div>
            <!-- Card Body -->
            <div class="card-body">
                <div class="chart-pie pt-4 pb-2">
                    <canvas id="sentiment_analysis"></canvas>
                </div>
                <div class="mt-4 text-center small">
                    <span class="mr-2">
                        <i class="fas fa-circle" style="color:#0220b7;"></i> Positive
                    </span>
                    <span class="mr-2">
                        <i class="fas fa-circle" style="color:#fe3737;"></i> Negative
                    </span>
                    <span class="mr-2">
                        <i class="fas fa-circle" style="color:#169a5b;"></i> Neutral
                    </span>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    var traffic_data = {!! json_encode($TrafficData) !!};
    var gender_data = {!! json_encode($GenderData) !!};
    var age_category_data = {!! json_encode($AgeCategoryData) !!};
    var emotion_data = {!! json_encode($EmotionData) !!};
    var mask_data = {!! json_encode($MaskData) !!};
    var race_data = {!! json_encode($RaceData) !!};
    var sentiment_data = {!! json_encode($SentimentData) !!};

    window.onload = function(){

      document.getElementById('month_picker').addEventListener('change', function() {
      var selectedDate = this.value; // Get the selected date value
      var url = "{{ route('HomePageViewLink', ['search_by_month' => ':date']) }}"; // Define the URL with a placeholder for the date parameter
      url = url.replace(':date', selectedDate); // Replace the placeholder with the selected date
      window.location.href = url; // Redirect to the updated URL

    });
    }

</script>

@endsection