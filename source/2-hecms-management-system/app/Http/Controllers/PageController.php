<?php

namespace App\Http\Controllers;


use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;

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

            $month_picker_display = "";

            if($search_by_month == '[FALSE]'){

                $search_data = $current_year = date('Y')."-".$current_month = date('m')."-".$current_month = date('d');
                $month_picker_display = date('Y')."-".date('m');
                
            }else{

                $month_picker_display = $search_by_month;
                $search_data = $search_by_month."-"."02";
               
            }

            $login_device_value_session = Session::get('DeviceValue');

            $traffic_data = DB::select("SELECT DAY(date) AS day, COUNT(*) AS count FROM data WHERE MONTH(date) = MONTH('$search_data') AND YEAR(date) = YEAR('$search_data') AND device_id = '$login_device_value_session' GROUP BY DAY(date) ORDER BY day ASC;");            
            $total_devices = DB::select("SELECT COUNT(*) as total_count FROM device WHERE device_id = '$login_device_value_session'");
            $total_incidents = DB::select("SELECT COUNT(*) as total_count FROM data WHERE device_id = '$login_device_value_session'");
            $total_elephants_detected = DB::select("SELECT SUM(number_of_elephant) as total_count FROM data WHERE device_id = '$login_device_value_session'");
            
            $device_info = DB::select("SELECT device_name, latitude, longitude from device WHERE device_id = '$login_device_value_session'");
            
            return view('home-page',['PageName' => 'Home Page', "YearMonth" => $month_picker_display , 'TrafficData' => $traffic_data, 'TotalDevices' => $total_devices, 'TotalIncidents' => $total_incidents, 'TotalElephantsDetected' => $total_elephants_detected, "LoginDeviceValue" => $login_device_value_session, "DeviceInfo" => $device_info]); 

        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }


    public function ViewDataManagementFunction(string $search_by_date){

        $login_access_session = Session::get('LoginAccess');
    
        if($login_access_session == '[SUPER_ADMIN]'){
    
            if($search_by_date == '[FALSE]'){
        
                $whole_data_management_data = DB::table('data')->orderBy('date', 'desc')->paginate(15);
                return view('data-management',['PageName' => 'Data Management', "type_of_search" => "[WHOLE_SEARCH]", "DataManagementData"=>$whole_data_management_data]); 
        
            }else{
        
                $date_wise_data_management_data = DB::table('data')->where('date', '=', $search_by_date)->orderBy('time', 'asc')->paginate(15);
        
                return view('data-management',['PageName' => 'Data Management', "type_of_search" => "[DATE_WISE_SEARCH]", "DataManagementData"=>$date_wise_data_management_data]); 
            }

        }else if($login_access_session == '[DEVICE_ADMIN]'){

            $login_device_value_session = Session::get('DeviceValue');
            $device_info = DB::select("SELECT device_name, latitude, longitude from device WHERE device_id = '$login_device_value_session'");
            
            if($search_by_date == '[FALSE]'){
        
                $whole_data_management_data =  DB::table('data')->where('device_id', '=', $login_device_value_session)->orderBy('date', 'desc')->paginate(15);
                return view('data-management',['PageName' => 'Data Management', "type_of_search" => "[WHOLE_SEARCH]", "DataManagementData"=>$whole_data_management_data, "LoginDeviceValue" => $login_device_value_session, "DeviceInfo" => $device_info]); 
        
            }else{
        
                $date_wise_data_management_data = DB::table('data')->where('date', '=', $search_by_date)->where('device_id', '=', $login_device_value_session)->orderBy('time', 'asc')->paginate(15);
                return view('data-management',['PageName' => 'Data Management', "type_of_search" => "[DATE_WISE_SEARCH]", "DataManagementData"=>$date_wise_data_management_data, "LoginDeviceValue" => $login_device_value_session, "DeviceInfo" => $device_info]); 
            }

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

            $login_device_value_session = Session::get('DeviceValue');
            $device_info = DB::select("SELECT * from device WHERE device_id = '$login_device_value_session'");
           
            return view('device-management',['PageName' => 'Device Preferences',  "LoginDeviceValue" => $login_device_value_session, "DeviceInfo" => $device_info]); 

        }else{
    
            return redirect()->route('IndexPageLink');
            
        }
        
    }

    public function ViewSettingsFunction(){
        
        $login_access_session = Session::get('LoginAccess');

        if($login_access_session == '[SUPER_ADMIN]'){

            return view('settings', ['PageName' => 'Settings']);
            
        }else if($login_access_session == '[DEVICE_ADMIN]'){

            $login_device_value_session = Session::get('DeviceValue');
            $device_info = DB::select("SELECT * from device WHERE device_id = '$login_device_value_session'");
           
            return view('settings', ['PageName' => 'Settings', "LoginDeviceValue" => $login_device_value_session, "DeviceInfo" => $device_info]);

        }else{

            return redirect()->route('IndexPageLink');
            
        }
        
    }
}