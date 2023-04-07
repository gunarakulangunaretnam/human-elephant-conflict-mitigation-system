<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Redirect;
use Illuminate\Support\Facades\Session;

class AuthenticationController extends Controller
{
    public function LoginFunction(Request $request){

        $this->validate($request, [
            'username' => 'required',
            'password' => 'required',
        ]);


        $user_entered_username =  $request->username;
        $user_entered_password =  $request->password;
        $account_type = $request->account_type;

        $username_from_db = "";
        $password_from_db = "";

       
        $user = DB::select("SELECT username, password FROM user_account WHERE account_type = '$account_type'");

        foreach($user as $u){

            $username_from_db = $u->username;
            $password_from_db = $u->password;

        }

         
        if($user_entered_username == $username_from_db && $user_entered_password == $password_from_db){

            if($account_type == "super_admin"){

                Session::put('LoginAccess', "[SUPER_ADMIN]");

            }else if($account_type == "device_admin"){
                
                Session::put('LoginAccess', '[DEVICE_ADMIN]');

            }else{
                
                return Redirect::to("/")->withErrors(['Someting went wrong! #ERROR 01']);
            }

            return redirect()->route('HomePageViewLink', ['search_by_month' => '[FALSE]']);


        }else{

            return Redirect::to("/")->withErrors(['The username or password is incorrect']);
        }

    }

    public function LogoutFunction(){
        Session::flush();
        return Redirect('/');
    }
}