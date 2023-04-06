<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Session;
use Illuminate\Support\Facades\Redirect;

class CurdController extends Controller
{

    public function SettingsChangeVoiceFunction(Request $request)
    {
        $login_access_session = Session::get('LoginAccess');
    
        if ($login_access_session == '[TRUE]') {
            $this->validate($request, [
                'language' => 'required',
            ]);
    
            $selected_language = ucfirst($request->language);
    
            DB::table('setting')
                ->where('_key', 'voice_lang')
                ->update(['_value' => $selected_language]);
    
            // Redirect back to the previous page with a success message
            return redirect()->back()->with('success', 'Language updated successfully.');
        } else {
            return abort(404);
        }
    }

    public function SettingsChangePasswordFunction(Request $request)
    {
        $login_access_session = Session::get('LoginAccess');
    
        if ($login_access_session == '[TRUE]') {
            $this->validate($request, [
                'current_password' => 'required',
                'new_password' => 'required',
                'confirm_password' => 'required',
            ]);


            $user_entered_current_password = $request->current_password;
            $user_entered_new_password = $request->new_password;
            $user_entered_confirm_password = $request->confirm_password;

            $current_server_password = DB::table('user')->value('password');


            if($user_entered_current_password == $current_server_password){

                if($user_entered_new_password == $user_entered_confirm_password){

                    DB::table('user')->update(['password' => $user_entered_new_password]);
                    return redirect()->back()->with('success', 'Password updated successfully.');
                    
                }else{

                    return redirect()->back()->with('error', 'The confirm password does not match.');
                }
                
            }{

                return redirect()->back()->with('error', 'The current password is wrong.');
            }

            
            // Redirect back to the previous page with a success message  
        } else {
            return abort(404);
        }
    }

    
    
}