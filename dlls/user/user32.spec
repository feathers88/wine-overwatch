@ stdcall ActivateKeyboardLayout(long long)
@ stdcall AdjustWindowRect(ptr long long)
@ stdcall AdjustWindowRectEx(ptr long long long)
@ stdcall AlignRects(ptr long long long)
# @ stub AllowForegroundActivation
@ stdcall AllowSetForegroundWindow (long)
@ stdcall AnimateWindow(long long long)
@ stdcall AnyPopup()
@ stdcall AppendMenuA(long long long ptr)
@ stdcall AppendMenuW(long long long ptr)
@ stdcall ArrangeIconicWindows(long)
@ stdcall AttachThreadInput(long long long)
@ stdcall BeginDeferWindowPos(long)
@ stdcall BeginPaint(long ptr)
@ stdcall BlockInput(long)
@ stdcall BringWindowToTop(long)
@ stdcall BroadcastSystemMessage(long ptr long long long) BroadcastSystemMessageA
@ stdcall BroadcastSystemMessageA(long ptr long long long)
# @ stub BroadcastSystemMessageExA
# @ stub BroadcastSystemMessageExW
@ stdcall BroadcastSystemMessageW(long ptr long long long)
# @ stub BuildReasonArray
@ stdcall CalcChildScroll(long long)
# @ stub CalcMenuBar
@ stdcall CallMsgFilter(ptr long) CallMsgFilterA
@ stdcall CallMsgFilterA(ptr long)
@ stdcall CallMsgFilterW(ptr long)
@ stdcall CallNextHookEx(long long long long)
@ stdcall CallWindowProcA(ptr long long long long)
@ stdcall CallWindowProcW(ptr long long long long)
@ stub CascadeChildWindows
@ stdcall CascadeWindows(long long ptr long ptr)
@ stdcall ChangeClipboardChain(long long)
@ stdcall ChangeDisplaySettingsA(ptr long)
@ stdcall ChangeDisplaySettingsExA(str ptr long long ptr)
@ stdcall ChangeDisplaySettingsExW(wstr ptr long long ptr)
@ stdcall ChangeDisplaySettingsW(ptr long)
@ stdcall ChangeMenuA(long long ptr long long)
@ stdcall ChangeMenuW(long long ptr long long)
@ stdcall CharLowerA(str)
@ stdcall CharLowerBuffA(str long)
@ stdcall CharLowerBuffW(wstr long)
@ stdcall CharLowerW(wstr)
@ stdcall CharNextA(str)
@ stdcall CharNextExA(long str long)
@ stdcall CharNextExW(long wstr long)
@ stdcall CharNextW(wstr)
@ stdcall CharPrevA(str str)
@ stdcall CharPrevExA(long str str long)
@ stdcall CharPrevExW(long wstr wstr long)
@ stdcall CharPrevW(wstr wstr)
@ stdcall CharToOemA(str ptr)
@ stdcall CharToOemBuffA(str ptr long)
@ stdcall CharToOemBuffW(wstr ptr long)
@ stdcall CharToOemW(wstr ptr)
@ stdcall CharUpperA(str)
@ stdcall CharUpperBuffA(str long)
@ stdcall CharUpperBuffW(wstr long)
@ stdcall CharUpperW(wstr)
@ stdcall CheckDlgButton(long long long)
@ stdcall CheckMenuItem(long long long)
@ stdcall CheckMenuRadioItem(long long long long long)
@ stdcall CheckRadioButton(long long long long)
@ stdcall ChildWindowFromPoint(long double)
@ stdcall ChildWindowFromPointEx(long double long)
@ stub CliImmSetHotKey
@ stub ClientThreadConnect
@ stub ClientThreadSetup
@ stdcall ClientToScreen(long ptr)
@ stdcall ClipCursor(ptr)
@ stdcall CloseClipboard()
@ stdcall CloseDesktop(long)
@ stdcall CloseWindow(long)
@ stdcall CloseWindowStation(long)
@ stdcall CopyAcceleratorTableA(long ptr long)
@ stdcall CopyAcceleratorTableW(long ptr long)
@ stdcall CopyIcon(long)
@ stdcall CopyImage(long long long long long)
@ stdcall CopyRect(ptr ptr)
@ stdcall CountClipboardFormats()
@ stdcall CreateAcceleratorTableA(ptr long)
@ stdcall CreateAcceleratorTableW(ptr long)
@ stdcall CreateCaret(long long long long)
@ stdcall CreateCursor(long long long long long ptr ptr)
@ stdcall CreateDesktopA(str str ptr long long ptr)
@ stdcall CreateDesktopW(wstr wstr ptr long long ptr)
@ stdcall CreateDialogIndirectParamA(long ptr long ptr long)
@ stdcall CreateDialogIndirectParamAorW(long ptr long ptr long long)
@ stdcall CreateDialogIndirectParamW(long ptr long ptr long)
@ stdcall CreateDialogParamA(long ptr long ptr long)
@ stdcall CreateDialogParamW(long ptr long ptr long)
@ stdcall CreateIcon(long long long long long ptr ptr)
@ stdcall CreateIconFromResource (ptr long long long)
@ stdcall CreateIconFromResourceEx(ptr long long long long long long)
@ stdcall CreateIconIndirect(ptr)
@ stdcall CreateMDIWindowA(ptr ptr long long long long long long long long)
@ stdcall CreateMDIWindowW(ptr ptr long long long long long long long long)
@ stdcall CreateMenu()
@ stdcall CreatePopupMenu()
# @ stub CreateSystemThreads
@ stdcall CreateWindowExA(long str str long long long long long long long long ptr)
@ stdcall CreateWindowExW(long wstr wstr long long long long long long long long ptr)
@ stdcall CreateWindowStationA(str long long ptr)
@ stdcall CreateWindowStationW(wstr long long ptr)
# @ stub CsrBroadcastSystemMessageExW
# @ stub CtxInitUser32
@ stdcall DdeAbandonTransaction(long long long)
@ stdcall DdeAccessData(long ptr)
@ stdcall DdeAddData(long ptr long long)
@ stdcall DdeClientTransaction(ptr long long long long long long ptr)
@ stdcall DdeCmpStringHandles(long long)
@ stdcall DdeConnect(long long long ptr)
@ stdcall DdeConnectList(long long long long ptr)
@ stdcall DdeCreateDataHandle(long ptr long long long long long)
@ stdcall DdeCreateStringHandleA(long str long)
@ stdcall DdeCreateStringHandleW(long wstr long)
@ stdcall DdeDisconnect(long)
@ stdcall DdeDisconnectList(long)
@ stdcall DdeEnableCallback(long long long)
@ stdcall DdeFreeDataHandle(long)
@ stdcall DdeFreeStringHandle(long long)
@ stdcall DdeGetData(long ptr long long)
@ stdcall DdeGetLastError(long)
@ stub DdeGetQualityOfService
@ stdcall DdeImpersonateClient(long)
@ stdcall DdeInitializeA(ptr ptr long long)
@ stdcall DdeInitializeW(ptr ptr long long)
@ stdcall DdeKeepStringHandle(long long)
@ stdcall DdeNameService(long long long long)
@ stdcall DdePostAdvise(long long long)
@ stdcall DdeQueryConvInfo(long long ptr)
@ stdcall DdeQueryNextServer(long long)
@ stdcall DdeQueryStringA(long long ptr long long)
@ stdcall DdeQueryStringW(long long ptr long long)
@ stdcall DdeReconnect(long)
@ stdcall DdeSetQualityOfService(long ptr ptr)
@ stdcall DdeSetUserHandle (long long long)
@ stdcall DdeUnaccessData(long)
@ stdcall DdeUninitialize(long)
@ stdcall DefDlgProcA(long long long long)
@ stdcall DefDlgProcW(long long long long)
@ stdcall DefFrameProcA(long long long long long)
@ stdcall DefFrameProcW(long long long long long)
@ stdcall DefMDIChildProcA(long long long long)
@ stdcall DefMDIChildProcW(long long long long)
# @ stub DefRawInputProc
@ stdcall DefWindowProcA(long long long long)
@ stdcall DefWindowProcW(long long long long)
@ stdcall DeferWindowPos(long long long long long long long long)
@ stdcall DeleteMenu(long long long)
@ stdcall DeregisterShellHookWindow (long)
@ stdcall DestroyAcceleratorTable(long)
@ stdcall DestroyCaret()
@ stdcall DestroyCursor(long)
@ stdcall DestroyIcon(long)
@ stdcall DestroyMenu(long)
# @ stub DestroyReasons
@ stdcall DestroyWindow(long)
# @ stub DeviceEventWorker
@ stdcall DialogBoxIndirectParamA(long ptr long ptr long)
@ stdcall DialogBoxIndirectParamAorW(long ptr long ptr long long)
@ stdcall DialogBoxIndirectParamW(long ptr long ptr long)
@ stdcall DialogBoxParamA(long str long ptr long)
@ stdcall DialogBoxParamW(long wstr long ptr long)
# @ stub DisableProcessWindowsGhosting
@ stdcall DispatchMessageA(ptr)
@ stdcall DispatchMessageW(ptr)
# @ stub DisplayExitWindowsWarnings
@ stdcall DlgDirListA(long str long long long)
@ stdcall DlgDirListComboBoxA(long ptr long long long)
@ stdcall DlgDirListComboBoxW(long ptr long long long)
@ stdcall DlgDirListW(long wstr long long long)
@ stdcall DlgDirSelectComboBoxExA(long ptr long long)
@ stdcall DlgDirSelectComboBoxExW(long ptr long long)
@ stdcall DlgDirSelectExA(long ptr long long)
@ stdcall DlgDirSelectExW(long ptr long long)
@ stdcall DragDetect(long double)
@ stub DragObject
@ stdcall DrawAnimatedRects(long long ptr ptr)
@ stdcall DrawCaption(long long ptr long)
@ stdcall DrawCaptionTempA(long long ptr long long str long)
@ stdcall DrawCaptionTempW(long long ptr long long wstr long)
@ stdcall DrawEdge(long ptr long long)
@ stdcall DrawFocusRect(long ptr)
@ stub DrawFrame
@ stdcall DrawFrameControl(long ptr long long)
@ stdcall DrawIcon(long long long long)
@ stdcall DrawIconEx(long long long long long long long long long)
@ stdcall DrawMenuBar(long)
@ stdcall DrawMenuBarTemp(long long long long long)
@ stdcall DrawStateA(long long ptr long long long long long long long)
@ stdcall DrawStateW(long long ptr long long long long long long long)
@ stdcall DrawTextA(long str long ptr long)
@ stdcall DrawTextExA(long str long ptr long ptr)
@ stdcall DrawTextExW(long wstr long ptr long ptr)
@ stdcall DrawTextW(long wstr long ptr long)
@ stdcall EditWndProc(long long long long) EditWndProcA
@ stdcall EmptyClipboard()
@ stdcall EnableMenuItem(long long long)
@ stdcall EnableScrollBar(long long long)
@ stdcall EnableWindow(long long)
@ stdcall EndDeferWindowPos(long)
@ stdcall EndDialog(long long)
@ stdcall EndMenu()
@ stdcall EndPaint(long ptr)
@ stub EndTask
# @ stub EnterReaderModeHelper
@ stdcall EnumChildWindows(long ptr long)
@ stdcall EnumClipboardFormats(long)
@ stdcall EnumDesktopWindows(long ptr ptr)
@ stdcall EnumDesktopsA(ptr ptr long)
@ stdcall EnumDesktopsW(ptr ptr long)
@ stub EnumDisplayDeviceModesA
@ stub EnumDisplayDeviceModesW
@ stdcall EnumDisplayDevicesA(ptr long ptr long)
@ stdcall EnumDisplayDevicesW(ptr long ptr long)
@ stdcall EnumDisplayMonitors(long ptr ptr long)
@ stdcall EnumDisplaySettingsA(str long ptr)
@ stdcall EnumDisplaySettingsExA(str long ptr long)
@ stdcall EnumDisplaySettingsExW(wstr long ptr long)
@ stdcall EnumDisplaySettingsW(wstr long ptr )
@ stdcall EnumPropsA(long ptr)
@ stdcall EnumPropsExA(long ptr long)
@ stdcall EnumPropsExW(long ptr long)
@ stdcall EnumPropsW(long ptr)
@ stdcall EnumThreadWindows(long ptr long)
@ stdcall EnumWindowStationsA(ptr long)
@ stdcall EnumWindowStationsW(ptr long)
@ stdcall EnumWindows(ptr long)
@ stdcall EqualRect(ptr ptr)
@ stdcall ExcludeUpdateRgn(long long)
@ stdcall ExitWindowsEx(long long)
@ stdcall FillRect(long ptr long)
@ stdcall FindWindowA(str str)
@ stdcall FindWindowExA(long long str str)
@ stdcall FindWindowExW(long long wstr wstr)
@ stdcall FindWindowW(wstr wstr)
@ stdcall FlashWindow(long long)
@ stdcall FlashWindowEx(ptr)
@ stdcall FrameRect(long ptr long)
@ stdcall FreeDDElParam(long long)
@ stdcall GetActiveWindow()
@ stdcall GetAltTabInfo(long long ptr ptr long) GetAltTabInfoA
@ stdcall GetAltTabInfoA(long long ptr ptr long)
@ stdcall GetAltTabInfoW(long long ptr ptr long)
@ stdcall GetAncestor(long long)
# @ stub GetAppCompatFlags2
@ stdcall GetAppCompatFlags(long)
@ stdcall GetAsyncKeyState(long)
@ stdcall GetCapture()
@ stdcall GetCaretBlinkTime()
@ stdcall GetCaretPos(ptr)
@ stdcall GetClassInfoA(long str ptr)
@ stdcall GetClassInfoExA(long str ptr)
@ stdcall GetClassInfoExW(long wstr ptr)
@ stdcall GetClassInfoW(long wstr ptr)
@ stdcall GetClassLongA(long long)
@ stdcall GetClassLongW(long long)
@ stdcall GetClassLongPtrA(long long)
@ stdcall GetClassLongPtrW(long long)
@ stdcall GetClassNameA(long ptr long)
@ stdcall GetClassNameW(long ptr long)
@ stdcall GetClassWord(long long)
@ stdcall GetClientRect(long long)
@ stdcall GetClipCursor(ptr)
@ stdcall GetClipboardData(long)
@ stdcall GetClipboardFormatNameA(long ptr long)
@ stdcall GetClipboardFormatNameW(long ptr long)
@ stdcall GetClipboardOwner()
@ stdcall GetClipboardSequenceNumber ()
@ stdcall GetClipboardViewer()
@ stdcall GetComboBoxInfo(long ptr)
@ stdcall GetCursor()
# @ stub GetCursorFrameInfo
@ stdcall GetCursorInfo(ptr)
@ stdcall GetCursorPos(ptr)
@ stdcall GetDC(long)
@ stdcall GetDCEx(long long long)
@ stdcall GetDesktopWindow()
@ stdcall GetDialogBaseUnits()
@ stdcall GetDlgCtrlID(long)
@ stdcall GetDlgItem(long long)
@ stdcall GetDlgItemInt(long long ptr long)
@ stdcall GetDlgItemTextA(long long ptr long)
@ stdcall GetDlgItemTextW(long long ptr long)
@ stdcall GetDoubleClickTime()
@ stdcall GetFocus()
@ stdcall GetForegroundWindow()
@ stdcall GetGUIThreadInfo(long ptr)
@ stdcall GetGuiResources(long long)
@ stdcall GetIconInfo(long ptr)
@ stub GetInputDesktop
@ stdcall GetInputState()
@ stdcall GetInternalWindowPos(long ptr ptr)
@ stdcall GetKBCodePage()
@ stdcall GetKeyNameTextA(long ptr long)
@ stdcall GetKeyNameTextW(long ptr long)
@ stdcall GetKeyState(long)
@ stdcall GetKeyboardLayout(long)
@ stdcall GetKeyboardLayoutList(long ptr)
@ stdcall GetKeyboardLayoutNameA(ptr)
@ stdcall GetKeyboardLayoutNameW(ptr)
@ stdcall GetKeyboardState(ptr)
@ stdcall GetKeyboardType(long)
@ stdcall GetLastActivePopup(long)
@ stdcall GetLastInputInfo(ptr)
# @ stub GetLayeredWindowAttributes
# @ stub GetListBoxInfo
@ stdcall GetMenu(long)
@ stdcall GetMenuBarInfo(long long long ptr)
@ stdcall GetMenuCheckMarkDimensions()
@ stdcall GetMenuContextHelpId(long)
@ stdcall GetMenuDefaultItem(long long long)
@ stub GetMenuIndex
@ stdcall GetMenuInfo(long ptr)
@ stdcall GetMenuItemCount(long)
@ stdcall GetMenuItemID(long long)
@ stdcall GetMenuItemInfoA(long long long ptr)
@ stdcall GetMenuItemInfoW(long long long ptr)
@ stdcall GetMenuItemRect(long long long ptr)
@ stdcall GetMenuState(long long long)
@ stdcall GetMenuStringA(long long ptr long long)
@ stdcall GetMenuStringW(long long ptr long long)
@ stdcall GetMessageA(ptr long long long)
@ stdcall GetMessageExtraInfo()
@ stdcall GetMessagePos()
@ stdcall GetMessageTime()
@ stdcall GetMessageW(ptr long long long)
@ stdcall GetMonitorInfoA(long ptr)
@ stdcall GetMonitorInfoW(long ptr)
# @ stub GetMouseMovePointsEx
@ stdcall GetNextDlgGroupItem(long long long)
@ stdcall GetNextDlgTabItem(long long long)
# @ stub GetNextQueueWindow
@ stdcall GetOpenClipboardWindow()
@ stdcall GetParent(long)
@ stdcall GetPriorityClipboardFormat(ptr long)
@ stdcall GetProcessDefaultLayout(ptr)
@ stdcall GetProcessWindowStation()
@ stdcall GetProgmanWindow ()
@ stdcall GetPropA(long str)
@ stdcall GetPropW(long wstr)
@ stdcall GetQueueStatus(long)
# @ stub GetRawInputBuffer
# @ stub GetRawInputData
# @ stub GetRawInputDeviceInfoA
# @ stub GetRawInputDeviceInfoW
# @ stub GetRawInputDeviceList
# @ stub GetReasonTitleFromReasonCode
# @ stub GetRegisteredRawInputDevices
@ stdcall GetScrollBarInfo(long long ptr)
@ stdcall GetScrollInfo(long long ptr)
@ stdcall GetScrollPos(long long)
@ stdcall GetScrollRange(long long ptr ptr)
@ stdcall GetShellWindow()
@ stdcall GetSubMenu(long long)
@ stdcall GetSysColor(long)
@ stdcall GetSysColorBrush(long)
@ stdcall GetSystemMenu(long long)
@ stdcall GetSystemMetrics(long)
@ stdcall GetTabbedTextExtentA(long str long long ptr)
@ stdcall GetTabbedTextExtentW(long wstr long long ptr)
@ stdcall GetTaskmanWindow ()
@ stdcall GetThreadDesktop(long)
@ stdcall GetTitleBarInfo(long ptr)
@ stdcall GetTopWindow(long)
@ stdcall GetUpdateRect(long ptr long)
@ stdcall GetUpdateRgn(long long long)
@ stdcall GetUserObjectInformationA (long long ptr long ptr)
@ stdcall GetUserObjectInformationW (long long ptr long ptr)
@ stdcall GetUserObjectSecurity (long ptr ptr long ptr)
# @ stub GetWinStationInfo
@ stdcall GetWindow(long long)
@ stdcall GetWindowContextHelpId(long)
@ stdcall GetWindowDC(long)
@ stdcall GetWindowInfo(long ptr)
@ stdcall GetWindowLongA(long long)
@ stdcall GetWindowLongPtrA(long long)
@ stdcall GetWindowLongPtrW(long long)
@ stdcall GetWindowLongW(long long)
# @ stub GetWindowModuleFileName
@ stdcall GetWindowModuleFileNameA(long ptr long)
@ stdcall GetWindowModuleFileNameW(long ptr long)
@ stdcall GetWindowPlacement(long ptr)
@ stdcall GetWindowRect(long ptr)
@ stdcall GetWindowRgn(long long)
# @ stub GetWindowRgnBox
@ stdcall GetWindowTextA(long ptr long)
@ stdcall GetWindowTextLengthA(long)
@ stdcall GetWindowTextLengthW(long)
@ stdcall GetWindowTextW(long ptr long)
@ stdcall GetWindowThreadProcessId(long ptr)
@ stdcall GetWindowWord(long long)
@ stdcall GrayStringA(long long ptr long long long long long long)
@ stdcall GrayStringW(long long ptr long long long long long long)
# @ stub HasSystemSleepStarted
@ stdcall HideCaret(long)
@ stdcall HiliteMenuItem(long long long long)
# @ stub IMPGetIMEA
# @ stub IMPGetIMEW
# @ stub IMPQueryIMEA
# @ stub IMPQueryIMEW
# @ stub IMPSetIMEA
# @ stub IMPSetIMEW
@ stdcall ImpersonateDdeClientWindow(long long)
@ stdcall InSendMessage()
@ stdcall InSendMessageEx(ptr)
@ stdcall InflateRect(ptr long long)
# @ stub InitSharedTable
# @ stub InitTask
# @ stub InitializeLpkHooks
# @ stub InitializeWin32EntryTable
@ stdcall InsertMenuA(long long long long ptr)
@ stdcall InsertMenuItemA(long long long ptr)
@ stdcall InsertMenuItemW(long long long ptr)
@ stdcall InsertMenuW(long long long long ptr)
@ stdcall InternalGetWindowText(long long long)
@ stdcall IntersectRect(ptr ptr ptr)
@ stdcall InvalidateRect(long ptr long)
@ stdcall InvalidateRgn(long long long)
@ stdcall InvertRect(long ptr)
@ stdcall IsCharAlphaA(long)
@ stdcall IsCharAlphaNumericA(long)
@ stdcall IsCharAlphaNumericW(long)
@ stdcall IsCharAlphaW(long)
@ stdcall IsCharLowerA(long)
@ stdcall IsCharLowerW(long)
@ stdcall IsCharUpperA(long)
@ stdcall IsCharUpperW(long)
@ stdcall IsChild(long long)
@ stdcall IsClipboardFormatAvailable(long)
@ stdcall IsDialogMessage(long ptr) IsDialogMessageA
@ stdcall IsDialogMessageA(long ptr)
@ stdcall IsDialogMessageW(long ptr)
@ stdcall IsDlgButtonChecked(long long)
# @ stub IsGUIThread
@ stdcall IsHungAppWindow(long)
# @ stub IsHungThread
@ stdcall IsIconic(long)
@ stdcall IsMenu(long)
@ stdcall IsRectEmpty(ptr)
# @ stub IsServerSideWindow
@ stdcall IsWinEventHookInstalled(long)
@ stdcall IsWindow(long)
@ stdcall IsWindowEnabled(long)
# @ stub IsWindowInDestroy
@ stdcall IsWindowUnicode(long)
@ stdcall IsWindowVisible(long)
@ stdcall IsZoomed(long)
@ stdcall KillSystemTimer(long long)
@ stdcall KillTimer(long long)
@ stdcall LoadAcceleratorsA(long str)
@ stdcall LoadAcceleratorsW(long wstr)
@ stdcall LoadBitmapA(long str)
@ stdcall LoadBitmapW(long wstr)
@ stdcall LoadCursorA(long str)
@ stdcall LoadCursorFromFileA(str)
@ stdcall LoadCursorFromFileW(wstr)
@ stdcall LoadCursorW(long wstr)
@ stdcall LoadIconA(long str)
@ stdcall LoadIconW(long wstr)
@ stdcall LoadImageA(long str long long long long)
@ stdcall LoadImageW(long wstr long long long long)
@ stdcall LoadKeyboardLayoutA(str long)
# @ stub LoadKeyboardLayoutEx
@ stdcall LoadKeyboardLayoutW(wstr long)
@ stdcall LoadLocalFonts()
@ stdcall LoadMenuA(long str)
@ stdcall LoadMenuIndirectA(ptr)
@ stdcall LoadMenuIndirectW(ptr)
@ stdcall LoadMenuW(long wstr)
@ stub LoadRemoteFonts
@ stdcall LoadStringA(long long ptr long)
@ stdcall LoadStringW(long long ptr long)
@ stdcall LockSetForegroundWindow (long)
@ stub LockWindowStation
@ stdcall LockWindowUpdate(long)
@ stub LockWorkStation
@ stdcall LookupIconIdFromDirectory(ptr long)
@ stdcall LookupIconIdFromDirectoryEx(ptr long long long long)
@ stub MBToWCSEx
# @ stub MB_GetString
@ stdcall MapDialogRect(long ptr)
@ stdcall MapVirtualKeyA(long long)
@ stdcall MapVirtualKeyExA(long long long)
@ stdcall MapVirtualKeyExW(long long long)
@ stdcall MapVirtualKeyW(long long)
@ stdcall MapWindowPoints(long long ptr long)
@ stdcall MenuItemFromPoint(long long double)
@ stub MenuWindowProcA
@ stub MenuWindowProcW
@ stdcall MessageBeep(long)
@ stdcall MessageBoxA(long str str long)
@ stdcall MessageBoxExA(long str str long long)
@ stdcall MessageBoxExW(long wstr wstr long long)
@ stdcall MessageBoxIndirectA(ptr)
@ stdcall MessageBoxIndirectW(ptr)
# @ stub MessageBoxTimeoutA
# @ stub MessageBoxTimeoutW
@ stdcall MessageBoxW(long wstr wstr long)
# @ stub ModifyAccess
@ stdcall ModifyMenuA(long long long long ptr)
@ stdcall ModifyMenuW(long long long long ptr)
@ stdcall MonitorFromPoint(double long)
@ stdcall MonitorFromRect(ptr long)
@ stdcall MonitorFromWindow(long long)
@ stdcall MoveWindow(long long long long long long)
@ stdcall MsgWaitForMultipleObjects(long ptr long long long)
@ stdcall MsgWaitForMultipleObjectsEx(long ptr long long long)
@ stdcall NotifyWinEvent(long long long long)
@ stdcall OemKeyScan(long)
@ stdcall OemToCharA(ptr ptr)
@ stdcall OemToCharBuffA(ptr ptr long)
@ stdcall OemToCharBuffW(ptr ptr long)
@ stdcall OemToCharW(ptr ptr)
@ stdcall OffsetRect(ptr long long)
@ stdcall OpenClipboard(long)
@ stdcall OpenDesktopA(str long long long)
@ stdcall OpenDesktopW(wstr long long long)
@ stdcall OpenIcon(long)
@ stdcall OpenInputDesktop(long long long)
@ stdcall OpenWindowStationA(str long long)
@ stdcall OpenWindowStationW(wstr long long)
@ stdcall PackDDElParam(long long long)
@ stdcall PaintDesktop(long)
# @ stub PaintMenuBar
@ stdcall PeekMessageA(ptr long long long long)
@ stdcall PeekMessageW(ptr long long long long)
@ stub PlaySoundEvent
@ stdcall PostMessageA(long long long long)
@ stdcall PostMessageW(long long long long)
@ stdcall PostQuitMessage(long)
@ stdcall PostThreadMessageA(long long long long)
@ stdcall PostThreadMessageW(long long long long)
# @ stub PrintWindow
@ stdcall PrivateExtractIconExA(str long ptr ptr long)
@ stdcall PrivateExtractIconExW(wstr long ptr ptr long)
@ stdcall PrivateExtractIconsA (str long long long ptr ptr long long)
@ stdcall PrivateExtractIconsW (wstr long long long ptr ptr long long)
# @ stub PrivateSetDbgTag
# @ stub PrivateSetRipFlags
@ stdcall PtInRect(ptr double)
@ stub QuerySendMessage
# @ stub QueryUserCounters
# @ stub RealChildWindowFromPoint
@ stdcall RealGetWindowClass(long ptr long) RealGetWindowClassA
@ stdcall RealGetWindowClassA(long ptr long)
@ stdcall RealGetWindowClassW(long ptr long)
# @ stub ReasonCodeNeedsBugID
# @ stub ReasonCodeNeedsComment
# @ stub RecordShutdownReason
@ stdcall RedrawWindow(long ptr long long)
@ stdcall RegisterClassA(ptr)
@ stdcall RegisterClassExA(ptr)
@ stdcall RegisterClassExW(ptr)
@ stdcall RegisterClassW(ptr)
@ stdcall RegisterClipboardFormatA(str)
@ stdcall RegisterClipboardFormatW(wstr)
@ stdcall RegisterDeviceNotificationA(long ptr long)
@ stdcall RegisterDeviceNotificationW(long ptr long)
@ stdcall RegisterHotKey(long long long long)
@ stdcall RegisterLogonProcess(long long)
# @ stub RegisterMessagePumpHook
@ stub RegisterNetworkCapabilities
# @ stub RegisterRawInputDevices
@ stub RegisterServicesProcess
@ stdcall RegisterShellHookWindow (long)
@ stdcall RegisterSystemThread(long long)
@ stdcall RegisterTasklist (long)
# @ stub RegisterUserApiHook
@ stdcall RegisterWindowMessageA(str)
@ stdcall RegisterWindowMessageW(wstr)
@ stdcall ReleaseCapture()
@ stdcall ReleaseDC(long long)
@ stdcall RemoveMenu(long long long)
@ stdcall RemovePropA(long str)
@ stdcall RemovePropW(long wstr)
@ stdcall ReplyMessage(long)
@ stub ResetDisplay
# @ stub ResolveDesktopForWOW
@ stdcall ReuseDDElParam(long long long long long)
@ stdcall ScreenToClient(long ptr)
@ stdcall ScrollChildren(long long long long)
@ stdcall ScrollDC(long long long ptr ptr long ptr)
@ stdcall ScrollWindow(long long long ptr ptr)
@ stdcall ScrollWindowEx(long long long ptr ptr long ptr long)
@ stdcall SendDlgItemMessageA(long long long long long)
@ stdcall SendDlgItemMessageW(long long long long long)
@ stdcall SendIMEMessageExA(long long)
@ stdcall SendIMEMessageExW(long long)
@ stdcall SendInput(long ptr long)
@ stdcall SendMessageA(long long long long)
@ stdcall SendMessageCallbackA(long long long long ptr long)
@ stdcall SendMessageCallbackW(long long long long ptr long)
@ stdcall SendMessageTimeoutA(long long long long long long ptr)
@ stdcall SendMessageTimeoutW(long long long long long long ptr)
@ stdcall SendMessageW(long long long long)
@ stdcall SendNotifyMessageA(long long long long)
@ stdcall SendNotifyMessageW(long long long long)
@ stub ServerSetFunctionPointers
@ stdcall SetActiveWindow(long)
@ stdcall SetCapture(long)
@ stdcall SetCaretBlinkTime(long)
@ stdcall SetCaretPos(long long)
@ stdcall SetClassLongA(long long long)
@ stdcall SetClassLongPtrA(long long long)
@ stdcall SetClassLongPtrW(long long long)
@ stdcall SetClassLongW(long long long)
@ stdcall SetClassWord(long long long)
@ stdcall SetClipboardData(long long)
@ stdcall SetClipboardViewer(long)
# @ stub SetConsoleReserveKeys
@ stdcall SetCursor(long)
@ stub SetCursorContents
@ stdcall SetCursorPos(long long)
@ stdcall SetDebugErrorLevel(long)
@ stdcall SetDeskWallPaper(str)
# @ stub SetDeskWallpaper
# @ stub SetDesktopBitmap
@ stdcall SetDlgItemInt(long long long long)
@ stdcall SetDlgItemTextA(long long str)
@ stdcall SetDlgItemTextW(long long wstr)
@ stdcall SetDoubleClickTime(long)
@ stdcall SetFocus(long)
@ stdcall SetForegroundWindow(long)
@ stdcall SetInternalWindowPos(long long ptr ptr)
@ stdcall SetKeyboardState(ptr)
@ stdcall SetLastErrorEx(long long)
@ stdcall SetLayeredWindowAttributes(ptr long long long)
@ stdcall SetLogonNotifyWindow(long long)
@ stdcall SetMenu(long long)
@ stdcall SetMenuContextHelpId(long long)
@ stdcall SetMenuDefaultItem(long long long)
@ stdcall SetMenuInfo(long ptr)
@ stdcall SetMenuItemBitmaps(long long long long long)
@ stdcall SetMenuItemInfoA(long long long ptr)
@ stdcall SetMenuItemInfoW(long long long ptr)
@ stdcall SetMessageExtraInfo(long)
@ stdcall SetMessageQueue(long)
@ stdcall SetParent(long long)
@ stdcall SetProcessDefaultLayout(long)
@ stdcall SetProcessWindowStation(long)
@ stdcall SetProgmanWindow (long)
@ stdcall SetPropA(long str long)
@ stdcall SetPropW(long wstr long)
@ stdcall SetRect(ptr long long long long)
@ stdcall SetRectEmpty(ptr)
@ stdcall SetScrollInfo(long long ptr long)
@ stdcall SetScrollPos(long long long long)
@ stdcall SetScrollRange(long long long long long)
@ stdcall SetShellWindow(long)
@ stdcall SetShellWindowEx (long long)
@ stdcall SetSysColors(long ptr ptr)
@ stdcall SetSysColorsTemp(ptr ptr long)
@ stdcall SetSystemCursor(long long)
@ stdcall SetSystemMenu(long long)
@ stdcall SetSystemTimer(long long long ptr)
@ stdcall SetTaskmanWindow (long)
@ stdcall SetThreadDesktop(long)
@ stdcall SetTimer(long long long ptr)
@ stdcall SetUserObjectInformationA(long long ptr long)
@ stdcall SetUserObjectInformationW(long long ptr long)
@ stdcall SetUserObjectSecurity(long ptr ptr)
@ stdcall SetWinEventHook(long long long ptr long long long)
@ stdcall SetWindowContextHelpId(long long)
@ stub SetWindowFullScreenState
@ stdcall SetWindowLongA(long long long)
@ stdcall SetWindowLongPtrA(long long long)
@ stdcall SetWindowLongPtrW(long long long)
@ stdcall SetWindowLongW(long long long)
@ stdcall SetWindowPlacement(long ptr)
@ stdcall SetWindowPos(long long long long long long long)
@ stdcall SetWindowRgn(long long long)
@ stdcall SetWindowStationUser(long long)
@ stdcall SetWindowText(long str) SetWindowTextA
@ stdcall SetWindowTextA(long str)
@ stdcall SetWindowTextW(long wstr)
@ stdcall SetWindowWord(long long long)
@ stdcall SetWindowsHookA(long ptr)
@ stdcall SetWindowsHookExA(long long long long)
@ stdcall SetWindowsHookExW(long long long long)
@ stdcall SetWindowsHookW(long ptr)
@ stdcall ShowCaret(long)
@ stdcall ShowCursor(long)
@ stdcall ShowOwnedPopups(long long)
@ stdcall ShowScrollBar(long long long)
@ stub ShowStartGlass
@ stdcall ShowWindow(long long)
@ stdcall ShowWindowAsync(long long)
# @ stub SoftModalMessageBox
@ stdcall SubtractRect(ptr ptr ptr)
@ stdcall SwapMouseButton(long)
@ stdcall SwitchDesktop(long)
@ stdcall SwitchToThisWindow(long long)
# @ stub SysErrorBox
@ stdcall SystemParametersInfoA(long long ptr long)
@ stdcall SystemParametersInfoW(long long ptr long)
@ stdcall TabbedTextOutA(long long long str long long ptr long)
@ stdcall TabbedTextOutW(long long long wstr long long ptr long)
@ stub TileChildWindows
@ stdcall TileWindows(long long ptr long ptr)
@ stdcall ToAscii(long long ptr ptr long)
@ stdcall ToAsciiEx(long long ptr ptr long long)
@ stdcall ToUnicode(long long ptr wstr long long)
@ stdcall ToUnicodeEx(long long ptr wstr long long long)
@ stdcall TrackMouseEvent(ptr)
@ stdcall TrackPopupMenu(long long long long long long ptr)
@ stdcall TrackPopupMenuEx(long long long long long ptr)
@ stdcall TranslateAccelerator(long long ptr) TranslateAcceleratorA
@ stdcall TranslateAcceleratorA(long long ptr)
@ stdcall TranslateAcceleratorW(long long ptr)
@ stdcall TranslateMDISysAccel(long ptr)
@ stdcall TranslateMessage(ptr)
# @ stub TranslateMessageEx
@ stdcall UnhookWinEvent(long)
@ stdcall UnhookWindowsHook(long ptr)
@ stdcall UnhookWindowsHookEx(long)
@ stdcall UnionRect(ptr ptr ptr)
@ stdcall UnloadKeyboardLayout(long)
@ stub UnlockWindowStation
@ stdcall UnpackDDElParam(long long ptr ptr)
@ stdcall UnregisterClassA(str long)
@ stdcall UnregisterClassW(wstr long)
@ stdcall UnregisterDeviceNotification(long)
@ stdcall UnregisterHotKey(long long)
# @ stub UnregisterMessagePumpHook
# @ stub UnregisterUserApiHook
@ stdcall UpdateLayeredWindow(long long ptr ptr long ptr long ptr long)
@ stub UpdatePerUserSystemParameters
@ stdcall UpdateWindow(long)
@ stdcall User32InitializeImmEntryTable(ptr)
@ stdcall UserClientDllInitialize(long long ptr) DllMain
@ stub UserHandleGrantAccess
# @ stub UserIsSystemResumeAutomatic
# @ stub UserLpkPSMTextOut
# @ stub UserLpkTabbedTextOut
@ stdcall UserRealizePalette(long)
@ stub UserRegisterWowHandlers
# @ stub UserSetDeviceHoldState
@ stdcall UserSignalProc(long long long long)
# @ stub VRipOutput
# @ stub VTagOutput
@ stdcall ValidateRect(long ptr)
@ stdcall ValidateRgn(long long)
@ stdcall VkKeyScanA(long)
@ stdcall VkKeyScanExA(long long)
@ stdcall VkKeyScanExW(long long)
@ stdcall VkKeyScanW(long)
@ stub WCSToMBEx
@ stdcall WINNLSEnableIME(long long)
@ stdcall WINNLSGetEnableStatus(long)
@ stdcall WINNLSGetIMEHotkey(long)
@ stub WNDPROC_CALLBACK
@ stdcall WaitForInputIdle(long long)
@ stdcall WaitMessage()
# @ stub Win32PoolAllocationStats
@ stdcall WinHelpA(long str long long)
@ stdcall WinHelpW(long wstr long long)
# @ stub WinOldAppHackoMatic
@ stdcall WindowFromDC(long)
@ stdcall WindowFromPoint(double)
# @ stub YieldTask
# @ stub _SetProcessDefaultLayout
@ stdcall keybd_event(long long long long)
@ stdcall mouse_event(long long long long long)
@ varargs wsprintfA(str str)
@ varargs wsprintfW(wstr wstr)
@ stdcall wvsprintfA(ptr str ptr)
@ stdcall wvsprintfW(ptr wstr ptr)

################################################################
# Wine extensions: Win16 functions that are needed by other dlls
#
@ stdcall CallWindowProc16(long long long long long)
@ stdcall CloseDriver16(long long long)
@ stdcall CreateDialogIndirectParam16(long ptr long long long)
@ stdcall DefDriverProc16(long long long long long)
@ stdcall DefWindowProc16(long long long long)
@ stdcall DestroyIcon32(long long)
@ stdcall DialogBoxIndirectParam16(long long long long long)
@ stdcall GetDriverModuleHandle16(long)
@ stdcall OpenDriver16(str str long)
@ stdcall SendDriverMessage16(long long long long)
@ stdcall UserYield16()

################################################################
# Wine dll separation hacks, these will go away, don't use them
#
@ cdecl HOOK_CallHooks(long long long long long)
@ cdecl USER_Unlock()
@ cdecl WINPOS_ActivateOtherWindow(long)
@ cdecl WINPOS_GetMinMaxInfo(long ptr ptr ptr ptr)
@ cdecl WINPOS_ShowIconTitle(long long)
@ cdecl WIN_GetPtr(long)
@ cdecl WIN_SetStyle(long long long)
