<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>AI Customer Analyzer</title>

    <!-- Custom fonts for this template-->
    <link href="{{ asset('dashboard-template-assets/vendor/fontawesome-free/css/all.min.css') }}" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="{{asset('dashboard-template-assets/css/sb-admin-2.min.css')}}" rel="stylesheet">

</head>

<body class="bg-gradient-primary">

    <div class="container" style="margin-top: 2.5%;">

        @if($errors->any())				
            @foreach ($errors->all() as $error)
                <div id="error-box" style="text-align:center;margin-top:20px;" class="alert alert-danger col-md-12 alert-dismissible fade show" role="alert">
                    <strong>{!!$error!!}</strong> 
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <script>
                    window.onload=function(){

                        $(window).on('load', function() {
                            $("#error-box").delay(3000).fadeOut();
                        })

                    }
                </script>

            @endforeach
        @endif

        <!-- Outer Row -->
        <div class="row justify-content-center">

            <div class="col-xl-10 col-lg-12 col-md-9">

                <div class="card o-hidden border-0 shadow-lg my-5">
                    <div class="card-body p-0">
                        <!-- Nested Row within Card Body -->
                        <div class="row">
                            <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                            <div class="col-lg-6">
                                <div class="p-5" style="height: 600px;">
                                    <div class="text-center" style="padding-bottom: 10%;">
                                        <h1 class="h4 text-gray-900 mb-4">AI Customer Analyzer <br> Login</h1>
                                    </div>
                                    <form class="user" method="POST" action="{{ route('LoginFunctionLink') }}">
                                        @csrf
                                        <div class="form-group" style="padding-bottom: 5%;">
                                            <input type="text" class="form-control form-control-user" id="exampleInputEmail" aria-describedby="emailHelp"
                                                   name="username" placeholder="Username" required>
                                        </div>
                                        <div class="form-group" style="padding-bottom: 5%;">
                                            <input type="password" class="form-control form-control-user" id="exampleInputPassword"
                                                   name="password" placeholder="Password" required>
                                        </div>
                                        <button type="submit" class="btn btn-primary btn-user btn-block">Login</button>
                                    </form>                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="{{ asset('dashboard-template-assets/vendor/jquery/jquery.min.js')}}"></script>
    <script src="{{ asset('dashboard-template-assets/vendor/bootstrap/js/bootstrap.bundle.min.js')}}"></script>

    <!-- Core plugin JavaScript-->
    <script src="{{ asset('dashboard-template-assets/vendor/jquery-easing/jquery.easing.min.js')}}"></script>

    <!-- Custom scripts for all pages-->
    <script src="{{ asset('dashboard-template-assets/js/sb-admin-2.min.js')}}"></script>

</body>

</html>