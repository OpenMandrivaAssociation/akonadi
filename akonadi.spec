Name: akonadi
Summary: An extensible cross-desktop storage service for PIM
Version: 0.80.0
Release: %mkrel 1
Url: http://websvn.kde.org/trunk/kdesupport/akonadi
License: LGPL v2+
Group: Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: %{name}-%{version}.tar.bz2
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: shared-mime-info >=  0.20
BuildRequires: kde4-macros
Conflicts: kde4-akonadi < 4.0.71-1

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.


%package common
Summary: %name common mime and dbus calls
Group: System/Libraries
Obsoletes: akonadi

%description common
%name common mime and dbus calls.

%files common
%defattr(-,root,root)
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/mime/packages/akonadi-mime.xml

#------------------------------------------------------

%define akonadiprotocolinternals_major 0
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n     %libakonadiprotocolinternals
Summary:        %name library
Group:          System/Libraries
Obsoletes:      %{_lib}akonadi_protocolinternals4 <= 4.0.70-1
Requires: %name-common

%description -n %libakonadiprotocolinternals
%name library.

%post -n %libakonadiprotocolinternals -p /sbin/ldconfig
%postun -n %libakonadiprotocolinternals -p /sbin/ldconfig

%files -n %libakonadiprotocolinternals
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

#------------------------------------------------------


%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Conflicts: kdepimlibs4-devel < 4.0.70-2
Conflicts: kdepim4-devel < 2:4.0.70-2
Requires: %libakonadiprotocolinternals

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
