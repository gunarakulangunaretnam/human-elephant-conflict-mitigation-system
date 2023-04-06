@extends('dashboard-layout.base-template')

@section('content')

<div class="container-fluid">

    @if ($errors->any())
        <div id="error-box" style="text-align:center;margin-top:20px;" class="alert alert-danger col-md-12 alert-dismissible fade show" role="alert">
            <ul>
                @foreach ($errors->all() as $error)
                    <li>{!! $error !!}</li>
                @endforeach
            </ul>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <script>
            window.onload=function(){
                $("#error-box").delay(3000).fadeOut();
            }
        </script>
    @endif



    @if(session('success'))
        <div id="success-box" style="text-align:center;margin-top:20px;" class="alert alert-success col-md-12 alert-dismissible fade show" role="alert">
            <strong>{{ session('success') }}</strong> 
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>

        <script>
            window.onload=function(){
                $("#success-box").delay(3000).fadeOut();
            }
        </script>
    @endif

    @if(session('error'))
    <div id="error-box" style="text-align:center;margin-top:20px;" class="alert alert-danger col-md-12 alert-dismissible fade show" role="alert">
        <strong>{{ session('error') }}</strong> 
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>

    <script>
        window.onload=function(){
            $("#error-box").delay(3000).fadeOut();
        }
    </script>
@endif

    <!-- Page Heading -->
    <div class="jumbotron">
        <div class="row">
            <div class="col-md-3 col-lg-3">
                <h4>Voice Settings</h4>
                <hr>
                <form class="user" method="POST" action="{{ route('SettingsChangeVoiceFunctionLink') }}">
                    @csrf <!-- Add the CSRF token field -->
                    <div class="input-group input-group-sm mb-3">
                        <div class="input-group-prepend">
                            <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Select Language:</span>
                        </div>
                        <select class="form-select form-control" name="language" aria-label="Small" aria-describedby="inputGroup-sizing-sm">
                            <option value="tamil" {{ $CurrentLanguage == 'Tamil' ? 'selected' : '' }}>Tamil</option>
                            <option value="sinhala" {{ $CurrentLanguage == 'Sinhala' ? 'selected' : '' }}>Sinhala</option>
                            <option value="english" {{ $CurrentLanguage == 'English' ? 'selected' : '' }}>English</option>
                        </select>                        
                    </div>
                    <button type="submit" class="btn btn-primary btn-sm">Change</button>
                </form>
            </div>
        </div>
    </div>

    <!-- Page Heading -->
    <div class="jumbotron">
        <div class="row">
            <div class="col-md-3 col-lg-3">
                <h4>Change Password</h4>
                <hr>

                <form class="user" method="POST" action="{{ route('SettingsChangePasswordFunctionLink') }}">
                    @csrf <!-- Add the CSRF token field -->
                    <div class="input-group input-group-sm mb-3">
                        <div class="input-group-prepend">
                            <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Current Password:</span>
                        </div>
                        <input type="password" name="current_password" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm" size="5" required>
                    </div>
                    <div class="input-group input-group-sm mb-3">
                        <div class="input-group-prepend">
                            <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">New Password:</span>
                        </div>
                        <input type="password" name="new_password" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm" size="5" required>
                    </div>
                    <div class="input-group input-group-sm mb-3">
                        <div class="input-group-prepend">
                            <span style="font-weight: bold;" class="input-group-text" id="inputGroup-sizing-sm">Confirm Password:</span>
                        </div>
                        <input type="password" name="confirm_password" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm" size="5" required>
                    </div>
                    <button type="submit" class="btn btn-primary btn-sm">Change</button>

                </form>
            </div>
                                     
        </div>
    </div>
        
</div>

@endsection