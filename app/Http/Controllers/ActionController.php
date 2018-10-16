<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ActionController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $fullPath =
        'python C:\Users\mk-da\Project\IAMT\public/login.py abcd 1234';
        system($fullPath, $outpara);
        return 0;
    }

    public function iine()
    {
        $fullPath =
        'python C:\Users\mk-da\Project\IAMT\public/login.py abcd 1234';
        system($fullPath, $outpara);
        return 0;
    }

    public function follow()
    {
        $fullPath =
        'python C:\Users\mk-da\Project\IAMT\public/login.py abcd 1234';
        system($fullPath, $outpara);
        return 0;
    }

    public function unfollow()
    {
        $fullPath =
        'python C:\Users\mk-da\Project\IAMT\public/login.py abcd 1234';
        system($fullPath, $outpara);
        return 0;
    }
}