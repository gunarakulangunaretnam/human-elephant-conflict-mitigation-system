@extends('dashboard-layout.base-template')
@section('content')

    <!-- Begin Page Content -->
    <div class="container-fluid">

        <!-- Page Heading -->

        <div class="row">
            <div class="card" style="width: 100%;">
                <div class="card-body">
                <div id="table" class="table-editable" style="font-size: 15px;">
                    <span class="table-add float-right mb-3 mr-2"
                    ><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#deviceModal">+Add New Device</button></span>
                    <table class="table table-bordered table-responsive-md table-hover text-center">
                    <thead>
                        <tr>
                        <th class="text-center">No</th>
                        <th class="text-center">Device ID</th>
                        <th class="text-center">Device Name</th>
                        <th class="text-center">Latitude</th>
                        <th class="text-center">Longitude</th>
                        <th class="text-center">Authority Email</th>
                        <th class="text-center">Authority Phone</th>
                        <th class="text-center">Username</th>
                        <th class="text-center">Password</th>
                        <th class="text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody>

                        <tr>
                           <td class="text-center">O1</td> 
                           <td class="text-center">er232</td> 
                           <td class="text-center">Batticaloa Kallady Device 1</td> 
                           <td class="text-center">32132432432432</td> 
                           <td class="text-center">432432432432432432</td> 
                           <td class="text-center">gunarakulan@gmail.com</td> 
                           <td class="text-center">0740001141</td> 
                           <td class="text-center">gunarakulan@gmail.com</td> 
                           <td class="text-center">0740001141</td> 
                           <td class="text-center" style="width: 20%;">
                            
                            <i title="View on Map" class="fa fa-globe fa-2x" style="color: darkblue;"
                                onmouseover="this.style.color='blue';" onmouseout="this.style.color='darkblue';"></i> &nbsp 
                            <a data-toggle="modal" data-target="#editDeviceModal"><i title="Edit" class="fa fa-pencil-square-o fa-2x" style="color: darkgreen;"
                                onmouseover="this.style.color='green';" onmouseout="this.style.color='darkgreen';"></i></a> &nbsp
                            <i title="Remove" class="fas fa-trash fa-2x" style="color: darkred;"
                                onmouseover="this.style.color='red';" onmouseout="this.style.color='darkred';"></i>                         

                            </td> 
                        </tr>
                       
                    </tbody>
                    </table>
                </div>
                </div>
            </div>
        </div>
            
        <div class="d-flex justify-content-center">
            
        </div>
        
        <!-- Device Modal -->
        <div class="modal fade" id="deviceModal" tabindex="-1" role="dialog" aria-labelledby="deviceModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="deviceModalLabel">Add New Device</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                </div>
                <div class="modal-body">
                <form>
                    <div class="form-group">
                    <label for="deviceId" class="col-form-label">Device ID:</label>
                    <input type="text" class="form-control" id="deviceId">
                    </div>
                    <div class="form-group">
                    <label for="deviceName" class="col-form-label">Device Name:</label>
                    <input type="text" class="form-control" id="deviceName">
                    </div>
                    <div class="form-group">
                    <label for="latitude" class="col-form-label">Latitude:</label>
                    <input type="text" class="form-control" id="latitude">
                    </div>
                    <div class="form-group">
                    <label for="longitude" class="col-form-label">Longitude:</label>
                    <input type="text" class="form-control" id="longitude">
                    </div>
                    <div class="form-group">
                        <label for="authorityEmail" class="col-form-label">Authority Email:</label>
                        <input type="email" class="form-control" id="authorityEmail">
                    </div>
                    <div class="form-group">
                        <label for="authorityPhone" class="col-form-label">Authority Phone:</label>
                        <input type="tel" class="form-control" id="authorityPhone">
                    </div>
                    <div class="form-group">
                        <label for="username" class="col-form-label">Username:</label>
                        <input type="text" class="form-control" id="username">
                    </div>
                    <div class="form-group">
                        <label for="password" class="col-form-label">Password:</label>
                        <input type="text" class="form-control" id="password">
                    </div>
                </form>
                </div>
                <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Add Device</button>
                </div>
            </div>
            </div>
        </div>

        <!-- Edit Device Modal -->
        <div class="modal fade" id="editDeviceModal" tabindex="-1" role="dialog" aria-labelledby="editDeviceModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                <h5 class="modal-title" id="editDeviceModalLabel">Edit Device</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                </div>
                <div class="modal-body">
                <form>
                    <div class="form-group">
                    <label for="editDeviceId" class="col-form-label">Device ID:</label>
                    <input type="text" class="form-control" id="editDeviceId">
                    </div>
                    <div class="form-group">
                    <label for="editDeviceName" class="col-form-label">Device Name:</label>
                    <input type="text" class="form-control" id="editDeviceName">
                    </div>
                    <div class="form-group">
                    <label for="editLatitude" class="col-form-label">Latitude:</label>
                    <input type="text" class="form-control" id="editLatitude">
                    </div>
                    <div class="form-group">
                    <label for="editLongitude" class="col-form-label">Longitude:</label>
                    <input type="text" class="form-control" id="editLongitude">
                    </div>
                    <div class="form-group">
                    <label for="editAuthorityEmail" class="col-form-label">Authority Email:</label>
                    <input type="email" class="form-control" id="editAuthorityEmail">
                    </div>
                    <div class="form-group">
                    <label for="editAuthorityPhone" class="col-form-label">Authority Phone:</label>
                    <input type="tel" class="form-control" id="editAuthorityPhone">
                    </div>
                    <div class="form-group">
                        <label for="username" class="col-form-label">Username:</label>
                        <input type="text" class="form-control" id="username">
                    </div>
                    <div class="form-group">
                        <label for="password" class="col-form-label">Password:</label>
                        <input type="text" class="form-control" id="password">
                    </div>
                </form>
                </div>
                <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save Changes</button>
                </div>
            </div>
            </div>
        </div>
  
  

    </div>

  

@endsection
