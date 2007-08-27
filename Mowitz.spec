%define name Mowitz
%define version 0.3.0
%define release %mkrel 5

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d


Summary:   Collection of widgets for X applications
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:       http://siag.nu/mowitz/
Source:    http://siag.nu/pub/mowitz/%{name}-%{version}.tar.bz2
Patch0:    Mowitz-0.3.0-overflow.patch
Patch1:    Mowitz-0.3.0-overflow2.patch
Patch2:    Mowitz-0.3.0-overflow3.patch
License:   GPL
Group:     System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Buildrequires: libXawM-devel XFree86-devel libxpm-devel  
Buildrequires: libneXtaw-devel glibc-static-devel autoconf2.5

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
Requires: %{libname} = %{version}
Provides: libMowitz-devel

%description -n %{libnamedev}
The Mowitz library contains a large collection of widgets for X applications
to use. It complements a widget set such as Xaw3d or neXtaw.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p0 -b .overflow
%patch1 -p0 -b .overflow2
%patch2 -p0 -b .overflow3

%build

%configure2_5x

%make

%install

%makeinstall

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/mowitz-config

rm -rf $RPM_BUILD_ROOT/usr/doc/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
