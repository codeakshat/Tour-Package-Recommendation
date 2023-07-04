import React from 'react';
import Layout from './Layout';
import aboutimg from './../image/about.png';
import { Link, } from "react-router-dom";

export default function about() {
    return (
    <Layout>
        <div className="container-fluid">
            <div className="row mt-4 mb-2">
                <div className="col-md-4 col-sm-6 col-xs-12">
                    <div className="border rounded shadow">
                        <div className="card m-2 ">
                            <h5 className="m-0 text-white font-weight-bold card-header bg-success"><i class="fa fa-tree" aria-hidden="true"></i>  WHO ARE WE</h5>
                            <img src={aboutimg} class="img-thumbnail" alt="" />
                            <div class="card-body m-0 p-0">
                                <p className="text-justify p-3">
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="col-md-4 col-sm-6 col-xs-12">
                    <div className="border rounded shadow">
                        <div className="card m-2 ">
                            <h5 className="m-0 text-white font-weight-bold card-header bg-success text-uppercase"><i class="fa fa-history" aria-hidden="true"></i>  Our History</h5>
                            <div class="card-body m-0 p-0 mt-2">
                            <a href="#" className='p-3 font-weight-bold text-warning'><i class="fa fa-clock-o" aria-hidden="true"></i> </a>
                                <p className="text-justify p-3">
                                <br />
                                <a href="#" className='font-weight-bold text-info'><i class="fa fa-clock-o" aria-hidden="true"></i> </a><br />
                               <br />
                              
                                <a href="#" className='font-weight-bold text-success'><i class="fa fa-clock-o" aria-hidden="true"></i></a><br />
                               
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="col-md-4 col-sm-6 col-xs-12">
                    <div className="border rounded shadow">
                        <div className="card m-2 ">
                            <h5 className="m-0 text-white font-weight-bold card-header bg-success text-uppercase"><i class="fa fa-graduation-cap" aria-hidden="true"></i> </h5>
                            <div class="card-body m-0 p-0">
                                <ul className="list-group">
                                    <li className="list-group-item text-info h6 font-weight-bold"></li>
                                    <li className="list-group-item text-info h6 font-weight-bold"></li>
                                    <li className="list-group-item text-info h6 font-weight-bold"></li>
                                    <li className="list-group-item text-danger h6 font-weight-bold text-center"></li>    
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
    )
}
