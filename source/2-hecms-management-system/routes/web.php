<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PageController;
use App\Http\Controllers\CurdController;
use App\Http\Controllers\AuthenticationController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [PageController::class, 'ViewIndexPageFunction'])->name("IndexPageLink");

Route::post('/login-function', [AuthenticationController::class, 'LoginFunction'])->name("LoginFunctionLink");

Route::get('/logout-function', [AuthenticationController::class, 'LogoutFunction'])->name("LogoutFunctionLink");

Route::get('/home-page-view/{search_by_month}', [PageController::class, 'ViewHomePageFunction'])->name("HomePageViewLink");

Route::get('/show-image/{id}', [PageController::class, 'ShowImageFunctionInNewPage'])->name("ShowImageFunctionInNewPageViewLink");

Route::get('/data-management-view/{search_by_date}', [PageController::class, 'ViewDataManagementFunction'])->name("DataManagementViewLink");

Route::get('/device-management-view', [PageController::class, 'ViewDeviceManagementFunction'])->name("DeviceManagementViewLink");

Route::post('/add-new-device', [PageController::class, 'AddNewDeviceFunction'])->name("AddNewDeviceLink");

Route::delete('/remove-device/{deviceId}', [PageController::class, 'RemoveDeviceFunction'])->name("removeDeviceLink");

Route::get('/settings-view', [PageController::class, 'ViewSettingsFunction'])->name("SettingsViewLink");

Route::post('/settings-change-voice', [CurdController::class, 'SettingsChangeVoiceFunction'])->name("SettingsChangeVoiceFunctionLink");

Route::post('/settings-change-password', [CurdController::class, 'SettingsChangePasswordFunction'])->name("SettingsChangePasswordFunctionLink");