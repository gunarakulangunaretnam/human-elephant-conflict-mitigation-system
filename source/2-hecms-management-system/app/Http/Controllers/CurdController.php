<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Validator;

class CurdController extends Controller
{
    public function AddNewDeviceFunction(Request $request){

        $login_access_session = Session::get('LoginAccess');

        if ($login_access_session == '[SUPER_ADMIN]') {

            // Define validation rules
            $rules = [
                'deviceId' => 'required|unique:device,device_id',
                'deviceName' => 'required',
                'latitude' => 'required',
                'longitude' => 'required',
                'authorityEmail' => 'required|email',
                'authorityPhone' => 'required',
                'username' => 'required|unique:user_account,username',
                'password' => 'required|min:6',
            ];            

            // Run validation
            $validator = Validator::make($request->all(), $rules);

            if ($validator->fails()) {
                // Redirect back with errors
                return redirect()->back()->withErrors($validator)->withInput();
            }else{

                 // Retrieve the form data
                $device_id = $request->input('deviceId');
                $device_name = $request->input('deviceName');
                $latitude = $request->input('latitude');
                $longitude = $request->input('longitude');
                $authority_email = $request->input('authorityEmail');
                $authority_phone = $request->input('authorityPhone');
                $username = $request->input('username');
                $password = $request->input('password');

                // Insert the data into the database
                DB::table('device')->insert([
                    'device_id' => $device_id,
                    'device_name' => $device_name,
                    'latitude' => $latitude,
                    'longitude' => $longitude,
                    'authority_email' => $authority_email,
                    'authority_phone' => $authority_phone
                ]);

                DB::table('user_account')->insert([
                    'username' => $username,
                    'password' => $password,
                    "account_type" => 'device_admin'
                ]);

                // Redirect back to the device management view
                return redirect()->route('DeviceManagementViewLink')->with('success', 'The device has been added successfully.');
                
            }

           
        } else {

            return redirect()->route('IndexPageLink');

        }
    }

    public function UpdateDeviceFunction(Request $request){
        
        $login_access_session = Session::get('LoginAccess');
    
        if ($login_access_session == '[SUPER_ADMIN]') {
            // Define validation rules
            $rules = [
                'editDeviceId' => 'required',
                'editDeviceName' => 'required',
                'editLatitude' => 'required',
                'editLongitude' => 'required',
                'editAuthorityEmail' => 'required|email',
                'editAuthorityPhone' => 'required',
                'editUsername' => 'required',
                'editPassword' => 'required|min:6',
            ];
    
            // Run validation
            $validator = Validator::make($request->all(), $rules);
    
            if ($validator->fails()) {
                // Redirect back with errors
                return redirect()->back()->withErrors($validator)->withInput();
            } else {
                // Retrieve the form data
                $device_id = $request->input('editDeviceId');
                $device_name = $request->input('editDeviceName');
                $latitude = $request->input('editLatitude');
                $longitude = $request->input('editLongitude');
                $authority_email = $request->input('editAuthorityEmail');
                $authority_phone = $request->input('editAuthorityPhone');
                $username = $request->input('editUsername');
                $password = $request->input('editPassword');
    
                // Update the device data in the database
                DB::table('device')->where('device_id', $device_id)->update([
                    'device_name' => $device_name,
                    'latitude' => $latitude,
                    'longitude' => $longitude,
                    'authority_email' => $authority_email,
                    'authority_phone' => $authority_phone
                ]);
    
                // Update the user account data in the database
                DB::table('user_account')->where('username', $username)->update([
                    'password' => $password
                ]);
    
                // Redirect back to the device management view
                return redirect()->route('DeviceManagementViewLink')->with('success', 'The device has been updated successfully.');
            }
        }else if($login_access_session == '[DEVICE_ADMIN]'){

            // Device Admin Logic Come Here

        } else {
            return redirect()->route('IndexPageLink');
        }
    }
    

    public function RemoveDeviceFunction($deviceId)
    {
        $login_access_session = Session::get('LoginAccess');

        if ($login_access_session == '[SUPER_ADMIN]') {

            DB::table('device')->where('device_id', $deviceId)->delete();
            DB::table('user_account')->where('username', $deviceId)->delete();

            return redirect()->back()->with('success', 'The device has been removed successfully.');

        }else{

            return redirect()->route('IndexPageLink');
            
        }
    }

    public function SettingsChangePasswordFunction(Request $request)
    {
        $login_access_session = Session::get('LoginAccess');
    
        if ($login_access_session == '[SUPER_ADMIN]') {
            $this->validate($request, [
                'current_password' => 'required',
                'new_password' => 'required',
                'confirm_password' => 'required',
            ]);


            $user_entered_current_password = $request->current_password;
            $user_entered_new_password = $request->new_password;
            $user_entered_confirm_password = $request->confirm_password;

            $current_server_password = DB::table('user_account')->value('password');


            if($user_entered_current_password == $current_server_password){

                if($user_entered_new_password == $user_entered_confirm_password){

                    DB::table('user_account')->where('account_type', 'super_admin')->update(['password' => $user_entered_new_password]);
                    return redirect()->back()->with('success', 'Password updated successfully.');
                    
                }else{

                    return redirect()->back()->with('error', 'The confirm password does not match.');
                }
                
            }{

                return redirect()->back()->with('error', 'The current password is wrong.');
            }

        }else if($login_access_session == '[DEVICE_ADMIN]'){

            // Device Admin Logic Come Here

        } else {
            return abort(404);
        }
    }
    
    
}