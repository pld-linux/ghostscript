Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpréteur et visualisateur PostScript & PDF
Summary(ja):	PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¡¦¥ì¥ó¥À¥é¡¼
Summary(pl):	Bezp³atny interpreter PostScriptu & PDF
Summary(tr):	PostScript & PDF yorumlayýcý ve gösterici
Name:		ghostscript
Version:	6.22
Release:	4
Vendor:		Aladdin Enterprises <bug-gs@aladdin.com>
Copyright:	Aladdin Free Public License
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	ftp://download.sourceforge.net/pub/sourceforge/ghostscript/%{name}-%{version}.tar.bz2
Source1:	http://www.ozemail.com.au/~geoffk/pdfencrypt/pdf_sec.ps
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-hpdj_driver.patch
URL:		http://www.ghostscript.com/
BuildRequires:	XFree86-devel
# Required by 'gdevvglb' device.
%ifnarch sparc sparc64
BuildRequires:	svgalib-devel
%endif
BuildRequires:	zlib-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpretor. It can render both PostScript
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
Ghostcript jest interpreterem PostScriptu, jêzyku u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF na szereg postaci wyj¶ciowych: drukarki (w³±czaj±c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalarý, X penceresinde
gösterebilir ve birçok yazýcýnýn (renkli yazýcýlar dahil) basabileceði
biçime getirebilir.

%prep
%setup -q -n gs%{version}
ln -s src/unix-gcc.mak Makefile
%patch0 -p1
%patch1 -p1
%setup -q -T -D -a 2 -n gs%{version}
ln -s jp* jpeg

%build
%{__make} \
	XCFLAGS="$RPM_OPT_FLAGS -DA4=1 -w" \
	XLDFLAGS="-s" \
	prefix=%{_prefix} \
	datadir=%{_datadir}/%{name} \
	mandir=%{_mandir} \
	docdir=%{_datadir}/doc/%{name}-%{version} \
	DEVICE_DEVS16="\$(DD)atx23.dev \$(DD)atx24.dev \$(DD)atx38.dev \
		\$(DD)fax.dev \
%ifnarch sparc sparc64
		\$(DD)vgalib.dev \
%endif
		\$(DD)x11_.dev \$(DD)x11alt_.dev \$(DD)x11cmyk2.dev \
		\$(DD)x11cmyk4.dev \$(DD)x11cmyk8.dev \$(DD)x11rg16x.dev \
		\$(DD)x11rg32x.dev \$(DD)fs600.dev \$(DD)lp2563.dev \
		\$(DD)oce9050.dev \$(DD)psdf.dev \$(DD)cgmmono.dev \
		\$(DD)cgm8.dev \$(DD)cgm24.dev \$(DD)miff24.dev \
		\$(DD)pcx2up.dev \$(DD)plan9bm.dev \$(DD)tfax.dev \
		\$(DD)tiffs.dev" \
	DEVICE_DEVS17="\$(DD)cfax.dev \$(DD)appledmp.dev \$(DD)iwhi.dev \
		\$(DD)iwlo.dev \$(DD)iwlq.dev \$(DD)ccr.dev \$(DD)cdj500.dev \
		\$(DD)declj250.dev \$(DD)dnj650c.dev \$(DD)lj4dith.dev \
		\$(DD)escp.dev \$(DD)djet500c.dev \$(DD)cljet5pr.dev \
		\$(DD)lj3100sw.dev \$(DD)coslw2p.dev \$(DD)coslwxl.dev \
		\$(DD)cp50.dev \$(DD)epson.dev \$(DD)eps9mid.dev \
		\$(DD)eps9high.dev \$(DD)ibmpro.dev \$(DD)epsonc.dev \
		\$(DD)ap3250.dev \$(DD)st800.dev \$(DD)stcolor.dev \
		\$(DD)cdj850.dev \$(DD)cdj670.dev \$(DD)cdj890.dev \
		\$(DD)cdj1600.dev \$(DD)cdj970.dev \$(DD)lj250.dev \
		\$(DD)paintjet.dev \$(DD)pjetxl.dev \$(DD)hl7x0.dev \
		\$(DD)imagen.dev \$(DD)jetp3852.dev \$(DD)lbp8.dev \
		\$(DD)lips3.dev \$(DD)lp8000.dev \$(DD)m8510.dev \
		\$(DD)necp6.dev \$(DD)lq850.dev \$(DD)lxm5700m.dev \
		\$(DD)oki182.dev \$(DD)okiibm.dev \$(DD)photoex.dev \
		\$(DD)r4081.dev \$(DD)sj48.dev \$(DD)t4693d2.dev \
		\$(DD)t4693d4.dev \$(DD)t4693d8.dev \$(DD)tek4696.dev \
		\$(DD)dfaxlow.dev \$(DD)dfaxhigh.dev \$(DD)cif.dev \
		\$(DD)inferno.dev \$(DD)mgrmono.dev \$(DD)mgrgray2.dev \
		\$(DD)mgrgray4.dev \$(DD)mgrgray8.dev \$(DD)mgr4.dev \
		\$(DD)mgr8.dev \$(DD)sgirgb.dev"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf1{2,3}.1

echo .so gs.1     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo .so ps2pdf.1 > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo .so ps2pdf.1 > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.htm
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{name}/lib/*.*
%dir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples/*
%config %verify(not size md5 mtime) %{_datadir}/%{name}/lib/Fontmap
%{_mandir}/man*/*
