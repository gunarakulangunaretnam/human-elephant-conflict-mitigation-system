@extends('dashboard-layout.base-template')
@section('content')

    <!-- Begin Page Content -->
    <div class="container-fluid">

        <!-- Page Heading -->

        <div class="jumbotron">
            <div class="row">
                <div class="col-md-3 offset-md-3 col-lg-3 offset-lg-4">
                    <div class="input-group input-group-sm mb-3">

                        <div style="text-align: center; margin-left:7%;">

                            <input type="radio" id="show_all_data" name="search-type" onclick="window.location.href='{{route('AudioDataViewLink', ['search_by_date' => '[FALSE]'])}}'"> Show all data |
                            <input type="radio" id="search_by_date" name="search-type"> <label>Search by date</label>
        
                          </div>

                        <div class="input-group-prepend">
                            <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Search by Date:</span>
                        </div>
                        <input type="date"  id="date_picker"  class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm">
                    </div>
                </div>
            </div>
        </div>
        

        <div class="row">

            <table style="background-color: white; border: 5px solid rgb(197, 189, 189); table-layout: fixed;" class="table table-hover table-light">
                <thead style="color:balck; background-color: #e3e5e8;">
                    <tr>
                    <th style="width: 60px;" scope="col">No</th>
                    <th scope="col">Date</th>
                    <th scope="col">Time</th>
                    <th scope="col">Stall No</th>
                    <th scope="col">Employee ID</th>
                    <th scope="col">Employee Name</th>
                    <th style="width: 350px;" scope="col">Transcription</th>
                    <th scope="col">Prediction</th>
                    </tr>
                </thead>
                <tbody>

                    @foreach($audio_data as $data)
                    <tr>
                        <td>{{ $data->auto_id }}</td>
                        <td>{{ $data->date }}</td>
                        <td>{{ $data->time }}</td>
                        <td>{{ $data->stall_no }}</td>
                        <td>{{ $data->employee_id }}</td>
                        <td>{{ $data->employee_name }}</td>
                        <td>{{ $data->transcription}}</td>

                        @if($data->prediction =='Negative')
                            <td style="color:red; font-weight:bold;">{{$data->prediction}}</td>
                        @elseif($data->prediction =='Positive')
                            <td style="color:green; font-weight:bold;">{{$data->prediction}}</td>
                        @elseif($data->prediction =='Neutral')
                            <td style="color:orange; font-weight:bold;">{{$data->prediction}}</td>
                        @else
                            <td>{{$data->prediction}}</td>
                        @endif
                    </tr>
                    @endforeach      
        
                </tbody>
                </table>

        </div>
            
    </div>

    <script>

        window.onload = function(){
      
          if ("{{$type_of_search}}" == "[WHOLE_SEARCH]"){
      
            document.getElementById("date_picker").disabled = true;
            document.getElementById("show_all_data").checked = true;
      
          }else if("{{$type_of_search}}" == "[DATE_WISE_SEARCH]"){
      
            document.getElementById("date_picker").disabled = false;
            document.getElementById("search_by_date").checked = true;
      
          }
      
          document.getElementById("search_by_date").onclick = function(){
      
            document.getElementById("date_picker").disabled = false;
      
          }
      
          document.getElementById('date_picker').addEventListener('change', function() {
            var selectedDate = this.value; // Get the selected date value
            var url = "{{ route('AudioDataViewLink', ['search_by_date' => ':date']) }}"; // Define the URL with a placeholder for the date parameter
            url = url.replace(':date', selectedDate); // Replace the placeholder with the selected date
            window.location.href = url; // Redirect to the updated URL
        });
      
        }
        
      </script>

@endsection
