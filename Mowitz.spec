%define major 0
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Collection of widgets for X applications
Name:		Mowitz
Version:	0.3.0
Release:	13
License:	GPL
Group:		System/Libraries
URL:		https://siag.nu/mowitz/
Source:		http://siag.nu/pub/mowitz/%{name}-%{version}.tar.bz2
Patch0:		Mowitz-0.3.0-overflow.patch
Patch1:		Mowitz-0.3.0-overflow2.patch
Patch2:		Mowitz-0.3.0-overflow3.patch
Patch3:		Mowitz-0.3.0-overflow4.patch
Patch4:		Mowitz-0.3.0-overflow5.patch
Patch5:		Mowitz-0.3.0-overflow6.patch
Patch6:		Mowitz-0.3.0-overflow7.patch
Patch7:		Mowitz-0.3.0-overflow8.patch
Patch8:		Mowitz-0.3.0-link.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	libneXtaw-devel

%description
The Mowitz library contains a large collection of widgets for X applications 
to use. It complements a widget set such as Xaw3d or neXtaw.

%package -n %{libname}
Summary:	Collection of widgets for X applications
Group:		System/Libraries

%description -n %{libname}
The Mowitz library contains a large collection of widgets for X applications 
to use. It complements a widget set such as Xaw3d or neXtaw.

%package -n %{libnamedev}
Summary:	Collection of widgets for X applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libMowitz-devel = %{version}-%{release}

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

%multiarch_binaries %{buildroot}%{_bindir}/mowitz-config

rm -rf %{buildroot}/usr/doc/

%files -n %{libname}
%{_libdir}/lib*.so.*
%{_datadir}/%{name}

%files -n %{libnamedev}
%{_bindir}/mowitz-config
%{multiarch_bindir}/mowitz-config
%_includedir/%name/
%{_libdir}/lib*.a
%{_libdir}/lib*.so

