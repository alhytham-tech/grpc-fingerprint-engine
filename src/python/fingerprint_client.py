#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-02-07 16:32:54
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : thelightfinder.blogspot.com
# @Version : 0.0.1

from typing import List
import grpc

import fingerprint_pb2 as fp_pb2
import fingerprint_pb2_grpc as fp_pb2_grpc
from fingerprint_pb2 import (EnrolledFMD, EnrollmentRequest, VerificationRequest, VerificationResponse, PreEnrolledFMD,)

"""
usage notes: add url base64 encoded fmds for testing purpose
in real code you will be getting the fmds from some source
which could 
"""
fmd1 = ""  # todo: add a pre_enrolled fmd1 for a finger
fmd2 = ""  # todo: add another pre_enrolled for the same finger
fmd3 = ""  # todo: add another pre_enrolled for the same finger
fmd4 = ""  # todo: add another pre_enrolled for the same finger

fmd5 = ""  # todo: add a finger enrolled fmd here
fmd6 = ""  # todo: add a different finger erolled fmd here

fmds_list = [fmd1, fmd2, fmd3, fmd4]
reg_fmd_list = [fmd5, fmd6]

def main():
    # testing on localhost
    with grpc.insecure_channel("localhost:4134") as channel:
        stub = fp_pb2_grpc.FingerPrintStub(channel)
        enroll_fingerprint(stub)
        verify_fingerprint(stub)
        check_duplicate_fingerprint(stub)


def enroll_fingerprint(stub):
    enrollment_request = EnrollmentRequest()
    
    for fmd in fmds_list:
        pre_enrollment_fmd = PreEnrolledFMD()
        pre_enrollment_fmd.base64PreEnrolledFMD = fmd
        enrollment_request.fmdCandidates.append(pre_enrollment_fmd)

    enrolled_fmd = stub.EnrollFingerprint(enrollment_request)
    
    print(enrolled_fmd.base64EnrolledFMD)


def verify_fingerprint(stub):
    
    pre_enrolled_fmd = PreEnrolledFMD()
    pre_enrolled_fmd.base64PreEnrolledFMD = fmd1

    enrolled_candidate_fmd = EnrolledFMD(base64EnrolledFMD=fmd5)
    
    verification_request = VerificationRequest(targetFMD=pre_enrolled_fmd)

    verification_request.fmdCandidates.append(enrolled_candidate_fmd)

    verification_response = stub.VerifyFingerprint(verification_request)

    print(verification_response.match)


def check_duplicate_fingerprint(stub):
    pre_enrolled_fmd = PreEnrolledFMD(base64PreEnrolledFMD=fmd2)

    verification_request = VerificationRequest(targetFMD=pre_enrolled_fmd)

    for reg_fmd in reg_fmd_list:
        verification_request.fmdCandidates.append(EnrolledFMD(base64EnrolledFMD=reg_fmd))
    
    check_duplicate_response = stub.CheckDuplicate(verification_request)

    print(check_duplicate_response.isDuplicate)


if __name__ == "__main__":
    main()
