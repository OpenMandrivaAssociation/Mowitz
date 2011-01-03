%define name Mowitz
%define version 0.3.0
%define release %mkrel 11

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary:   Collection of widgets for X applications
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:       http://siag.nu/mowitz/
Source:    http://siag.nu/pub/mowitz/%{name}-%{version}.tar.bz2
Patch0:    Mowitz-0.3.0-overflow.patch
Patch1:    Mowitz-0.3.0-overflow2.patch
Patch2:    Mowitz-0.3.0-overflow3.patch
Patch3:    Mowitz-0.3.0-overflow4.patch
Patch4:    Mowitz-0.3.0-overflow5.patch
Patch5:    Mowitz-0.3.0-overflow6.patch
Patch6:    Mowitz-0.3.0-overflow7.patch
Patch7:    Mowitz-0.3.0-overflow8.patch
Patch8:    Mowitz-0.3.0-link.patch
License:   GPL
Group:     System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libx11-devel
BuildRequires: libxpm-devel
BuildRequires: libxext-devel
BuildRequires: libxaw-devel
BUildRequires: libxmu-devel
BUildRequires: libxt-devel
BuildRequires: libneXtaw-devel

%description
The Mowitz library contains a large collection of widgets for X applications 
to use. It complements a widget set such as Xaw3d or neXtaw.

%package -n %{libname}
Summary: Collection of widgets for X applications
Group: System/Libraries

%description -n %{libname}
The Mowitz library contains a large collection of widgets for X applications 
to use. It complements a widget set such as Xaw3d or neXtaw.

%package -n %{libnamedev}
Summary:  Collection of widgets for X applications
Group:    Development/C
Requires: %{libname} = %{version}-%{release}
Provides: libMowitz-devel = %{version}-%{release}
Obsoletes: %{_lib}Mowitz0-devel

%description -n %{libnamedev}
The Mowitz library contains a large collection of widgets for X applications
to use. It complements a widget set such as Xaw3d or neXtaw.

%prep
%setup -q
%patch0 -p0 -b .overflow
%patch1 -p0 -b .overflow2
%patch2 -p0 -b .overflow3
%patch3 -p0 -b .overflow4
%patch4 -p0 -b .overflow5
%patch5 -p0 -b .overflow6
%patch6 -p0 -b .overflow7
%patch7 -p0 -b .overflow8
%patch8 -p0 -b .link

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/mowitz-config

rm -rf $RPM_BUILD_ROOT/usr/doc/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL ChangeLog README
%doc doc/*.gif
%doc doc/*.html doc/List* doc/Sl*
%{_libdir}/lib*.so.*
%_datadir/%name

%files -n %{libnamedev}
%defattr(-,root,root)
%_bindir/*
%multiarch %{multiarch_bindir}/*
%_includedir/%name/
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/lib*.la
