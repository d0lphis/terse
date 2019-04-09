﻿//============================================================================
// Name        : FTPServer.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <Windows.h>
//#include "stdafx.h"
#include <iostream>
#include <winsock2.h>
#pragma comment(lib,"ws2_32.lib")
#include <Windows.h>

using namespace std;

#define  PORT 4000
#define  IP_ADDRESS "192.168.1.145"

DWORD WINAPI ClientThread(LPVOID lpParameter)
{
    SOCKET CientSocket = (SOCKET)lpParameter;
    int Ret = 0;
    char RecvBuffer[MAX_PATH];

    while ( true )
    {
        memset(RecvBuffer, 0x00, sizeof(RecvBuffer));
        Ret = recv(CientSocket, RecvBuffer, MAX_PATH, 0);
        if ( Ret == 0 || Ret == SOCKET_ERROR )
        {
            cout<<"Client exited!"<<endl;
            break;
        }
        cout<<"Client message received:"<<RecvBuffer<<endl;
    }

    return 0;
}

int main(int argc, char* argv[])
{
    WSADATA  Ws;
    SOCKET ServerSocket, CientSocket;
    struct sockaddr_in LocalAddr, ClientAddr;
    int Ret = 0;
    int AddrLen = 0;
    HANDLE hThread = NULL;

    //Init Windows Socket
    if ( WSAStartup(MAKEWORD(2,2), &Ws) != 0 )
    {
        cout<<"Init Windows Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    //Create Socket
    ServerSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if ( ServerSocket == INVALID_SOCKET )
    {
        cout<<"Create Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    LocalAddr.sin_family = AF_INET;
    LocalAddr.sin_addr.s_addr = inet_addr(IP_ADDRESS);
    LocalAddr.sin_port = htons(PORT);
    memset(LocalAddr.sin_zero, 0x00, 8);

    //Bind Socket
    Ret = bind(ServerSocket, (struct sockaddr*)&LocalAddr, sizeof(LocalAddr));
    if ( Ret != 0 )
    {
        cout<<"Bind Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    Ret = listen(ServerSocket, 10);
    if ( Ret != 0 )
    {
        cout<<"listen Socket Failed::"<<GetLastError()<<endl;
        return -1;
    }

    cout<<"Server started"<<endl;

    while ( true )
    {
        AddrLen = sizeof(ClientAddr);
        CientSocket = accept(ServerSocket, (struct sockaddr*)&ClientAddr, &AddrLen);
        if ( CientSocket == INVALID_SOCKET )
        {
            cout<<"Accept Failed::"<<GetLastError()<<endl;
            break;
        }

        cout<<"Client connection::"<<inet_ntoa(ClientAddr.sin_addr)<<":"<<ClientAddr.sin_port<<endl;

        hThread = CreateThread(NULL, 0, ClientThread, (LPVOID)CientSocket, 0, NULL);
        if ( hThread == NULL )
        {
            cout<<"Create Thread Failed!"<<endl;
            break;
        }

        CloseHandle(hThread);
    }

    closesocket(ServerSocket);
    closesocket(CientSocket);
    WSACleanup();

    return 0;
}
