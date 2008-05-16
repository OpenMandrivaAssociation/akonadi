%define svn   808261

Name: akonadi
Summary: An extensible cross-desktop storage service for PIM
Version: 0.80.0
Release: %mkrel 3.%svn.4
Url: http://websvn.kde.org/trunk/kdesupport/akonadi
License: LGPL v2+
Group: Networking/WWW
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0:       %{name}-%{version}.%svn.tar.bz2
Patch0:        akonadi-0.80.0-fix-automoc-detection.patch
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
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*
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

#---------------------------------------------------------------------

%define akonadiprivate_major 0
%define libakonadiprivate %mklibname akonadiprivate %{akonadiprivate_major}

%package -n %libakonadiprivate
Summary: %name library
Group: System/Libraries
Obsoletes:      %{_lib}akonadiprivate4 <= 4.0.70-1

%description -n %libakonadiprivate
%name library.

%post -n %libakonadiprivate -p /sbin/ldconfig
%postun -n %libakonadiprivate -p /sbin/ldconfig

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
%setup -q  -n %name
%patch0 -p0

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
