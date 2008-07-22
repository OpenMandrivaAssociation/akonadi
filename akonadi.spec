Name: akonadi
Summary: An extensible cross-desktop storage service for PIM
Version: 1.0.0
Release: %mkrel 1
Url: http://pim.kde.org/akonadi/
License: LGPL v2+
Group: Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: http://akonadi.omat.nl/%{name}-%{version}.tar.bz2
BuildRequires: qt4-devel >= 4.4.0
BuildRequires: shared-mime-info >=  0.20
BuildRequires: kde4-macros
BuildRequires: libxslt-proc
BuildRequires: libxml2-utils
BuilDrequires: automoc
Conflicts:     kde4-akonadi < 4.0.71-1

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
%{_kde_bindir}/*
%{_kde_datadir}/config/akonadi
%{_datadir}/dbus-1/services/*
%{_datadir}/mime/packages/akonadi-mime.xml
%{_kde_datadir}/dbus-1/interfaces/*.xml

#------------------------------------------------------

%define akonadiprotocolinternals_major 1
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n     %libakonadiprotocolinternals
Summary:        %name library
Group:          System/Libraries
Obsoletes:      %{_lib}akonadi_protocolinternals4 <= 4.0.70-1
Requires: %name-common

%description -n %libakonadiprotocolinternals
%name library.

%if %mdkversion < 200900
%post -n %libakonadiprotocolinternals -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libakonadiprotocolinternals -p /sbin/ldconfig
%endif

%files -n %libakonadiprotocolinternals
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

#---------------------------------------------------------------------

%define akonadiprivate_major 1
%define libakonadiprivate %mklibname akonadiprivate %{akonadiprivate_major}

%package -n %libakonadiprivate
Summary: %name library
Group: System/Libraries
Obsoletes:      %{_lib}akonadiprivate4 <= 4.0.70-1

%description -n %libakonadiprivate
%name library.

%if %mdkversion < 200900
%post -n %libakonadiprivate -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libakonadiprivate -p /sbin/ldconfig
%endif

%files -n %libakonadiprivate
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprivate.so.%{akonadiprivate_major}*

#------------------------------------------------------

%package   devel
Summary:   Devel stuff for %name
Group:     Development/KDE and Qt
Conflicts: kdepimlibs4-devel < 4.0.70-2
Conflicts: kdepim4-devel < 2:4.0.70-2
Requires:  %libakonadiprotocolinternals = %version
Requires:  %libakonadiprivate = %version

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/pkgconfig/akonadi.pc

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
rm -rf %buildroot

cd build
make DESTDIR=%buildroot install

%if %mdkversion < 200900
mkdir -p %buildroot/%_datadir/dbus-1
mv %buildroot/%{_kde_datadir}/dbus-1/services %buildroot/%_datadir/dbus-1
mv %buildroot/%{_kde_datadir}/mime %buildroot/%_datadir/
%endif

%clean
rm -rf "%{buildroot}"
