%define name xdvi
%define version 22.84
%define release %mkrel 5

Summary: An X viewer for DVI files
Name: %{name}
Version: %{version}
Release: %{release}
Url: http://math.berkeley.edu/~vojta/xdvi.html
License: GPL
Group: Publishing
Source0: ftp://dante.ctan.org/pub/tex/dviware/xdvi/%{name}-%{version}.tar.bz2
Source1: icons-%{name}.tar.bz2
Conflicts: tetex-xdvi
Requires: tetex

BuildRequires: X11-devel

%description
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

This xdvi does not come from TeTex distribution.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
%makeinstall

mkdir -p %buildroot%_iconsdir
mkdir -p %buildroot%_menudir

( cd %buildroot%_iconsdir
  tar xjvf %SOURCE1 )

cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/xdvi" needs="X11" \
icon="dvi.png" section="Office/Publishing" title="XDvi" \
longtitle="DVI files viewer" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XDvi
Comment=DVI files viewer
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Office-Publishing;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL FAQ README
%_bindir/*
%_mandir/man?/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_menudir/%name
%_iconsdir/dvi.png
%_liconsdir/dvi.png
%_miconsdir/dvi.png


