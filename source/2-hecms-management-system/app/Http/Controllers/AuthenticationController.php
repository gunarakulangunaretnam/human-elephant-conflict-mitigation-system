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

        $username_from_db = "";
        $password_from_db = "";

       
        $user = DB::select('SELECT username, password FROM user');

        foreach($user as $u){

            $username_from_db = $u->username;
            $password_from_db = $u->password;

        }

         
        if($user_entered_username == $username_from_db && $user_entered_password == $password_from_db){

            Session::put('LoginAccess', '[TRUE]');

            $login_access_session = Session::get('LoginAccess');

            # If password & username correct, redirect to home-page.blade.php
            if($login_access_session == '[TRUE]'){

                return redirect()->route('HomePageViewLink', ['search_by_month' => '[FALSE]']);
            }


        }else{

            return Redirect::to("/")->withErrors(['The username or password is incorrect']);
        }

    }

    public function LogoutFunction(){
        Session::flush();
        return Redirect('/');
    }
}