Name: akonadi
Summary: An extensible cross-desktop storage service for PIM
Version:        0.80.0
Release:        %mkrel 0.1
Url:            http://websvn.kde.org/trunk/kdesupport/akonadi
License:        LGPL v2+
Group:          Networking/WWW
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  qt4-devel >= 4.4.0

%description
An extensible cross-desktop storage service for PIM data and meta data providing
concurrent read, write, and query access.

%files
%defattr(-,root,root)
%{_kde_bindir}/akonadi_control
%{_kde_bindir}/akonadictl
%{_kde_bindir}/akonadiserver
%{_kde_datadir}/config/akonadi/mysql-global.conf
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/org.kde.Akonadi.Control.service
%{_datadir}/mime/packages/akonadi-mime.xml

#---------------------------------------------------------------------

%define akonadiprivate_major 0
%define libakonadiprivate %mklibname akonadiprivate %{akonadiprivate_major}

%package -n %libakonadiprivate
Summary: %name library
Group: System/Libraries

%description -n %libakonadiprivate
%name library.

%post -n %libakonadiprivate -p /sbin/ldconfig
%postun -n %libakonadiprivate -p /sbin/ldconfig

%files -n %libakonadiprivate
%defattr(-,root,root,-)
%_kde_libdir/libakonadiprivate.so.%{akonadiprivate_major}*

#------------------------------------------------------

%define akonadiprotocolinternals_major 0
%define libakonadiprotocolinternals %mklibname akonadiprotocolinternals %{akonadiprotocolinternals_major}

%package -n %libakonadiprotocolinternals
Summary: %name library
Group: System/Libraries

%description -n %libakonadiprotocolinternals
%name library.

%post -n %libakonadiprotocolinternals -p /sbin/ldconfig
%postun -n %libakonadiprotocolinternals -p /sbin/ldconfig

%files -n %libakonadiprotocolinternals
%defattr(-,root,roo,-)
%_kde_libdir/libakonadiprotocolinternals.so.%{akonadiprotocolinternals_major}*

#------------------------------------------------------


%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt

%description  devel
This package contains header files needed if you wish to build applications
based on %name

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
