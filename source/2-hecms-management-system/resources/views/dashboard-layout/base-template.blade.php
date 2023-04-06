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
    <link href="{{ asset('dashboard-template-assets/vendor/fontawesome-free/css/all.min.css')}}" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="{{ asset('dashboard-template-assets/css/sb-admin-2.min.css')}}" rel="stylesheet">

</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
        <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

            <!-- Sidebar - Brand -->
            <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
                <div class="sidebar-brand-text mx-3">AI Customer Analyzer</div>
            </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Divider -->
            <hr class="sidebar-divider">


            <!-- Nav Item - Pages Collapse Menu -->
            <li class="nav-item {{ $PageName == 'Home Page' ? 'active' : '' }}">
                <a class="nav-link collapsed" href="{{ route('HomePageViewLink', ['search_by_month' => '[FALSE]']) }}">
                    <i class="fas fa-fw fa-home"></i>
                    <span>Home Page</span>
                </a>
            </li>

            <li class="nav-item {{ $PageName == 'Vision Data' ? 'active' : '' }}">
                <a class="nav-link collapsed" href="{{route('VisionDataViewLink', ['search_by_date' => '[FALSE]']) }}">
                    <i class="fas fa-fw fa-video"></i>
                    <span>Vision Data</span>
                </a>
            </li>

            <li class="nav-item {{ $PageName == 'Audio Data' ? 'active' : '' }}">
                <a class="nav-link collapsed" href="{{ route('AudioDataViewLink', ['search_by_date' => '[FALSE]']) }}" >
                    <i class="fas fa-fw fa-music"></i>
                    <span>Audio Data</span>
                </a>
            </li>


            <li class="nav-item {{ $PageName == 'Settings' ? 'active' : '' }}">
                <a class="nav-link collapsed" href="{{ route('SettingsViewLink') }}">
                    <i class="fas fa-fw fa-cog"></i>
                    <span>Settings</span>
                </a>
            </li>

            <li class="nav-item">
                <a class="nav-link collapsed" href="{{ route('LogoutFunctionLink') }}" >
                    <i class="fas fa-fw fa-power-off"></i>
                    <span>Logout</span>
                </a>
            </li>

            <!-- Divider -->
            <hr class="sidebar-divider d-none d-md-block">

            <!-- Sidebar Toggler (Sidebar) -->
            <div class="text-center d-none d-md-inline">
                <button class="rounded-circle border-0" id="sidebarToggle"></button>
            </div>

        </ul>
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->
                <nav class="navbar navbar-expand text-center navbar-light bg-white topbar mb-4 static-top text-center shadow">

                    <div style="width: 100%;">

                        <h1 style="text-align: center !important;">{{ $PageName }}</h1>

                    </div>
      

                </nav>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->

                <div id="main-content">
                  
                    @yield('content')

                </div>            

            </div>
                <!-- /.container-fluid -->
            <!-- Footer -->
            <footer class="sticky-footer bg-white">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto">
                        <span>© 2023 AI Customer Analyzer | All rights reserved | Created by <a href="https://www.linkedin.com/in/gunarakulangunaretnam/" target="_blank">Gunarakulan Gunaretnam</a></span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">×</span>
                    </button>
                </div>
                <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                    <a class="btn btn-primary" href="login.html">Logout</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="{{asset('dashboard-template-assets/vendor/jquery/jquery.min.js')}}"></script>
    <script src= "{{asset('dashboard-template-assets/vendor/bootstrap/js/bootstrap.bundle.min.js"')}}"></script>

    <!-- Core plugin JavaScript-->
    <script src="{{asset('dashboard-template-assets/vendor/jquery-easing/jquery.easing.min.js')}}"></script>

    <!-- Custom scripts for all pages-->
    <script src="{{asset('dashboard-template-assets/js/sb-admin-2.min.js')}}"></script>

    <!-- Page level plugins -->
    <script src="{{asset('dashboard-template-assets/vendor/chart.js/Chart.min.js')}}"></script>

    <!-- Page level custom scripts -->
    <script src="{{asset('dashboard-template-assets/js/demo/chart-area-demo.js')}}"></script>
    <script src="{{asset('dashboard-template-assets/js/demo/chart-pie-demo.js')}}"></script>

</body>

</html>