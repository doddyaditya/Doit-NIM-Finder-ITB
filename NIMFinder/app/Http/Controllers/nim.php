<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Crypt;

class nim extends Controller
{
    public function index() {
        return view('search', ['user' => []]);
    }

    public function search(Request $request) {
        $this->validate($request,[
            'id' => 'required'
        ]);
        $id = $request->id;
        $user = DB::table('user')
            ->where('nim_tpb', 'like', '%'. $id . '%')
            ->orWhere('nim_jur', 'like', '%'. $id . '%')
            ->orWhere(DB::raw('lower(nama)'), 'like', '%'. strtolower($id). '%')
            ->orderByRaw('nim_tpb ASC','nim_jur ASC')
            ->paginate(20);
        return view('search', ['user' => $user, 'id' => $id]);
    }
}
