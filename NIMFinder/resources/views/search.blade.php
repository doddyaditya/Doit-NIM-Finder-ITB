<!DOCTYPE html>
<html>
    <head>
        <meta name="_token" content="{{ csrf_token() }}">
        <title>Doit NIM Finder</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    </head>
    <body>
        <div>
            <nav class="navbar navbar-dark bg-dark" style='width:100%'>
                <a class="navbar-brand" href='/'>
                    <span class="align-middle font-weight-bold font-italic">Doit NIM Finder</span>  
                </a>
            </nav>
            <form action='/search' method='GET' class='form-group form-control-lg' style='margin-top:16px'>
                @if(sizeof($user) != 0)
                    <input type='text' name='id' placeholder='Input name or NIM' value={{$id}}>
                @else
                    <input type='text' name='id' placeholder='Input name or NIM'>
                @endif
                <input class='btn btn-primary btn-md' type='submit' value='Search'>
            </form>

            @if(sizeof($user) != 0)
                <div class='table-responsive-sm' style='margin-left:16px;margin-right:16px'>
                    <table class='table table-bordered table-hover'>
                        <thead class='thead-dark'>
                            <tr>
                                <th style="width: 33.33%" scope='col'>Nama</th>
                                <th style="width: 33.33%" scope='col'>NIM</th>
                                <th style="width: 33.33%" scope='col'>Jurusan</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach($user as $u)
                            <tr>
                                <td>{{$u->nama}}</td>
                                @if(strpos($u->nim_jur,'00000000') === false)
                                    <td>{{$u->nim_tpb . "\t" . "-" . "\t" . $u->nim_jur}}</td>
                                @else
                                    <td>{{$u->nim_tpb}}</td>
                                @endif
                                <td>{{$u->jur}}</td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                </div>
                <nav aria-label="Page navigation example">
                    <ul class="pagination justify-content-center pagination-md">
                        @if($user->currentPage()<2)
                            <li class="page-item disabled">
                                <a class="page-link" tabindex="-1">Previous</a>
                            </li>
                        @else
                            <li class="page-item">
                                <a class="page-link" href="{{$user->previousPageUrl() . '&id=' . $id}}" tabindex="-1">Previous</a>
                            </li>
                            <li class="page-item">
                                <a class="page-link" href="{{$user->previousPageUrl() . '&id=' . $id}}">{{$user->currentPage()-1}}</a>
                            </li>
                        @endif
                        <li class="page-item active"><span class="page-link">{{$user->currentPage()}}<span class="sr-only">(current)</span></span></li>
                        @if($user->currentPage() < $user->lastPage())
                            <li class="page-item">
                                <a class="page-link" href="{{$user->nextPageUrl() . '&id=' . $id}}">{{$user->currentPage()+1}}</a>
                            </li>
                            <li class="page-item">
                                <a class="page-link" href="{{$user->nextPageUrl() . '&id=' . $id}}">Next</a>
                            </li>
                        @else
                            <li class="page-item disabled"><a class="page-link">Next</a></li>
                        @endif
                    </ul>
                </nav>
            @endif
        </div>
    </body>
</html>