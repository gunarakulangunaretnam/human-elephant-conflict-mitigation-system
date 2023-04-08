<?php

namespace App\Http\Controllers;


use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Validator;

class PageController extends Controller
{
    public function ViewIndexPageFunction(){

        return view('index'); 

    }

    public function ViewHomePageFunction(string $search_by_month){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[SUPER_ADMIN]'){


            $month_picker_display = "";

            if($search_by_month == '[FALSE]'){

                $search_data = $current_year = date('Y')."-".$current_month = date('m')."-".$current_month = date('d');
                $month_picker_display = date('Y')."-".date('m');
            }else{

                $month_picker_display = $search_by_month;
                $search_data = $search_by_month."-"."02";
               
            }
            $traffic_data = DB::select("SELECT DAY(date) AS day, COUNT(*) AS count FROM data WHERE MONTH(date) = MONTH('$search_data') AND YEAR(date) = YEAR('$search_data') GROUP BY DAY(date) ORDER BY day ASC;");            
            $total_devices = DB::select("SELECT COUNT(*) as total_count FROM device");
            $total_incidents = DB::select("SELECT COUNT(*) as total_count FROM data");
            $total_elephants_detected = DB::select("SELECT SUM(number_of_elephant) as total_count FROM data");
            
            return view('home-page',['PageName' => 'Home Page', "YearMonth" => $month_picker_display , 'TrafficData' => $traffic_data, 'TotalDevices' => $total_devices, 'TotalIncidents' => $total_incidents, 'TotalElephantsDetected' => $total_elephants_detected]); 

            
        }else if($login_access_session == '[DEVICE_ADMIN]'){

            // Device Admin Logic Come Here

        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }


    public function ViewDataManagementFunction(string $search_by_date){

        $login_access_session = Session::get('LoginAccess');
    
        if($login_access_session == '[SUPER_ADMIN]'){
    
            if($search_by_date == '[FALSE]'){
        
                $whole_data_management_data = DB::table('data')->paginate(15);
                return view('data-management',['PageName' => 'Data Management', "type_of_search" => "[WHOLE_SEARCH]", "DataManagementData"=>$whole_data_management_data]); 
        
            }else{
        
                $date_wise_data_management_data = DB::table('data')->where('date', '=', $search_by_date)->paginate(15);
        
                return view('data-management',['PageName' => 'Data Management', "type_of_search" => "[DATE_WISE_SEARCH]", "DataManagementData"=>$date_wise_data_management_data]); 
            }

        }else if($login_access_session == '[DEVICE_ADMIN]'){

            // Device Admin Logic Come Here

        }else{
            
            return redirect()->route('IndexPageLink');
       
        }
    }

    public function ShowImageFunctionInNewPage($id){

        $login_access_session = Session::get('LoginAccess');
        
        if($login_access_session == '[SUPER_ADMIN]' || $login_access_session == '[DEVICE_ADMIN]'){

            $image_data_db = DB::select("SELECT elephant_image from data WHERE auto_id = '$id'");
            $imageData = base64_encode($image_data_db[0]->elephant_image);
            $imageData = base64_decode($imageData);
            return response($imageData)->header('Content-Type', 'image/jpeg');
            
        }
        
    }

    public function ViewDeviceManagementFunction(){
    
        $login_access_session = Session::get('LoginAccess');
    
        if($login_access_session == '[SUPER_ADMIN]'){

            
            $device_management_data = DB::table('device')
            ->join('user_account', 'device.device_id', '=', 'user_account.username')
            ->select('device.*', 'user_account.*')
            ->paginate(15);

            $unique_id = substr(uniqid(), 0, 10);

            return view('device-management',['PageName' => 'Device Management', 'UniqueID' => $unique_id, "DeviceManagementData" => $device_management_data]); 
            
        }else if($login_access_session == '[DEVICE_ADMIN]'){

            // Device Admin Logic Come Here

        }else{
    
            return redirect()->route('IndexPageLink');
            
        }
        
    }

    public function AddNewDeviceFunction(Request $request){

        $login_access_session = Session::get('LoginAccess');

        if ($login_access_session == '[SUPER_ADMIN]') {

            // Define validation rules
            $rules = [
                'deviceId' => 'required|unique:device,device_id',
                'deviceName' => 'required',
                'latitude' => 'required|numeric',
                'longitude' => 'required|numeric',
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

    

    public function ViewSettingsFunction(){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[TRUE]'){

            $current_language = DB::table('setting')->where('_key', 'voice_lang')->value('_value');


            return view('settings', [
                'PageName' => 'Settings',
                'CurrentLanguage' => $current_language
            ]);
            
        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }
}