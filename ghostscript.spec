#
# Conditional build:
%bcond_without cups	# without CUPS support
%bcond_with gimpprint	# with gimp-print support (requires gimp-print < 2.3)
%bcond_with svga	# with svgalib display support (vgalib and lvga256 devices)
%bcond_without omni	# without omni support
%bcond_with gtk2	# experimental GTK+ 2 support

Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpréteur et visualisateur PostScript & PDF
Summary(ja):	PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¡¦¥ì¥ó¥À¥é¡¼
Summary(pl):	Bezp³atny interpreter i renderer PostScriptu i PDF
Summary(tr):	PostScript & PDF yorumlayýcý ve gösterici
Name:		ghostscript
%define gnu_ver 7.07
Version:	%{gnu_ver}.1
Release:	0.6
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/espgs/espgs-%{version}-source.tar.bz2
# Source0-md5:	d30bf5c09f2c7caa8291f6305cf03044
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
# Source2-md5:	dbd5f3b47ed13132f04c685d608a7547
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source5-md5:	9b5953aa0cc155f4364f20036b848585
Patch0:		%{name}-missquotes.patch
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-time_h.patch
Patch3:		%{name}-ijs_cflags.patch
Patch4:		%{name}-gdevcd8-fixes.patch
Patch5:		%{name}-gtk+2.patch
URL:		http://www.ghostscript.com/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
# for gsx
#BuildRequires:	gtk+-devel
BuildRequires:	glib%{?with_gtk2:2}-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
# Required by 'gdevvglb' device.
%ifarch %{ix86} alpha ppc
%{?with_svga:BuildRequires:	svgalib-devel}
%endif
# for documentation regeneration
BuildRequires:	tetex
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	docbook-style-dsssl
%{?with_gimpprint:BuildRequires:	gimp-print-devel}
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl
PostScript als auch PDF-konforme Dateien an Geräte ausgeben, zu denen
ein X-Fenster, viele Druckerformate (einschließlich Support für
Farbdrucker) und gängige Grafikdateiformate zählen.

%description -l fr
Ghostscript est un interpréteur PostScript. Il peut rendre des
fichiers PostScript ou PDF sur des périphériques dont une fenêtre X,de
nombreux types d'imprimantes (dont un support pour imprimantes
couleur), et des formats de fichiers graphiques populaires.

%description -l ja
Ghostscript ¤Ï PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤Ç¤¹¡£¥Ý¥¹¥È¥¹¥¯¥ê¥×¥È¤È PDF
¤ò¥ì¥ó¥À¥ê¥ó¥°¤·¡¢X window ¤äÂ¾¤Î¥×¥ê¥ó¥¿¥Õ¥©¡¼¥Þ¥Ã¥È¤Ç½ÐÎÏ
¤·¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ÏÆüËÜ¸ìÂÐ±þ¤·¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Ghostcript jest interpreterem PostScriptu, jêzyka u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF na szereg postaci wyj¶ciowych: drukarki (w³±czaj±c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalarý, X penceresinde
gösterebilir ve birçok yazýcýnýn (renkli yazýcýlar dahil) basabileceði
biçime getirebilir.

%package gtk
Summary:	Ghostscript with Gtk+ console
Summary(pl):	Ghostscript z konsol± Gtk+
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description gtk
Ghostscript with Gtk+ console.

%description gtk -l pl
Ghostscript z konsol± Gtk+.

%package devel
Summary:	libgs header files
Summary(pl):	Pliki nag³ówkowe libgs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libgs - ghostscript shared library.

%description devel -l pl
Pliki nag³ówkowe libgs - wspó³dzielonej biblioteki ghostscript.

%package ijs-devel
Summary:	IJS development files
Summary(pl):	Pliki dla programistów IJS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description ijs-devel
IJS development files.

%description ijs-devel -l pl
Pliki do tworzenia programów z u¿yciem biblioteki IJS.

%package ijs-static
Summary:	Static libijs library
Summary(pl):	Statyczna biblioteka IJS
Group:		Development/Libraries
Requires:	%{name}-ijs-devel = %{version}

%description ijs-static
Static libijs library.

%description ijs-static -l pl
Statyczna wersja biblioteki IJS.

%package -n cups-filter-pstoraster
Summary:	CUPS filter for support non-postscript printers
Summary(pl):	Filtr CUPS-a obs³uguj±cy drukarki niepostscriptowe
Group:		Applications/Printing
Requires:	cups >= 1.1.16
Requires:	%{name} = %{version}

%description -n cups-filter-pstoraster
CUPS filter for support non-postscript printers.

%description -n cups-filter-pstoraster -l pl
Filtr CUPS-a obs³uguj±cy drukarki niepostscriptowe.

%prep
%setup -q -n espgs-%{version} -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if %{with gtk2}
%patch5 -p1
%endif
ln -sf jp* jpeg

%build
cp -f %{_datadir}/automake/config.sub .
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -DA4"
export CFLAGS
%configure \
	--with-drivers=ALL%{?with_svga:,vgalib,lvga256} \
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1" \
	--with-ijs \
	--with%{!?with_gimpprint:out}-gimp-print \
	%{!?with_cups:--disable-cups} \
	--with%{!?with_omni:out}-omni \
	--with-x
cd ijs
%{__autoconf}
%configure
cd ..

#%%{__make} so \
%{__make} \
	docdir=%{_defaultdocdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/ghostscript/lib,%{_libdir},%{_includedir}}

#%%{__make} soinstall \
%{__make} install \
	install_prefix=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

cd ijs
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
cd ..

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

#install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj,eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

#mv -f $RPM_BUILD_ROOT%{_bindir}/{gsc,gs}
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

install -d $RPM_BUILD_ROOT%{_includedir}/ps
#install src/{iapi,errors}.h $RPM_BUILD_ROOT%{_includedir}/ps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/[bdeflpsux]*
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/wftopfa
%attr(755,root,root) %{_bindir}/gs[^x]*
%attr(755,root,root) %{_bindir}/ijs_client_example
#%attr(755,root,root) %{_libdir}/libgs.so.*.*
%attr(755,root,root) %{_libdir}/libijs.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.*
%dir %{_datadir}/%{name}/%{gnu_ver}
%dir %{_datadir}/%{name}/%{gnu_ver}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{name}/%{gnu_ver}/lib/*.*
%{_datadir}/%{name}/%{gnu_ver}/lib/CIDFnmap
%config %verify(not size md5 mtime) %{_datadir}/%{name}/%{gnu_ver}/lib/Fontmap
%{_datadir}/%{name}/%{gnu_ver}/examples
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(pl) %{_mandir}/pl/man*/*

#%files gtk
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/gsx

#%files devel
#%defattr(644,root,root,755)
#%%{_includedir}/ps
#%%{_libdir}/libgs.so

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%{_includedir}/ijs

%files ijs-static
%defattr(644,root,root,755)
%{_libdir}/libijs.a

%if %{with cups}
%files -n cups-filter-pstoraster
%defattr(644,root,root,755)
%(cups-config --serverroot)/*
%attr(755,root,root) %(cups-config --serverbin)/filter/*
%endif
