@extends('dashboard-layout.base-template')

@section('content')

<div class="container-fluid">

    <!-- Page Heading -->

    <div class="row">
    
        <!-- Area Chart -->
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">            
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Elephant Traffic Tracker</h6>

                    <div class="col-md-3 offset-md-3 col-lg-3 offset-lg-4">
                        <div class="input-group input-group-sm mb-3">
                            <div class="input-group-prepend">
                                <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Filter by Month:</span>
                            </div>
                            <input type="month" value="{{$YearMonth}}" id="month_picker" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm">
                        </div>
                     </div>
                    
                </div>
                <!-- Card Body -->
                <div class="card-body">
                    <div class="chart-area">
                        <canvas id="customer-chart"></canvas>
                    </div>
                </div>
            </div>
        </div>

          <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-4 col-md-6 mb-4">
                <div class="card border-left-primary shadow h-100 py-2">
                    <div class="card-body">
                        <div class="row no-gutters align-items-center">
                            <div class="col mr-2">
                                <div class="text-lg font-weight-bold text-primary text-uppercase mb-1" style="text-align: center;">Total Devices</div>
                                <div class="text-md h5 mb-0 font-weight-bold text-gray-800" style="text-align: center;">{{ reset($TotalDevices)->total_count}}</div>
                            </div>
                            <div class="col-auto">
                                <i class="fas fa-microchip fa-2x text-gray-300"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Earnings (Monthly) Card Example -->
            <div class="col-xl-4 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                    <div class="row no-gutters align-items-center">
                        <div class="col mr-2">
                            <div class="text-lg font-weight-bold text-primary text-uppercase mb-1" style="text-align: center;">Total Incidents</div>
                            <div class="text-md h5 mb-0 font-weight-bold text-gray-800" style="text-align: center;">{{reset($TotalIncidents)->total_count}}</div>
                        </div>
                        <div class="col-auto">
                            <i class="fas fa-camera fa-2x text-gray-300"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Earnings (Monthly) Card Example -->
        <div class="col-xl-4 col-md-6 mb-4">
            <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                    <div class="row no-gutters align-items-center">
                        <div class="col mr-2">
                            <div class="text-lg font-weight-bold text-primary text-uppercase mb-1" style="text-align: center;">Total Elephants Detected</div>
                            <div class="text-md h5 mb-0 font-weight-bold text-gray-800" style="text-align: center;">{{reset($TotalElephantsDetected)->total_count}}</div>
                        </div>
                        <div class="col-auto">
                            <i class="fas fa-camera fa-2x text-gray-300"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>



<script>
    var traffic_data = {!! json_encode($TrafficData) !!};
    
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